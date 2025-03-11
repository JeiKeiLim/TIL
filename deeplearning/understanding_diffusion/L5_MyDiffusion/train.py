import argparse
import os

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from tqdm import tqdm

from model import ContextUnet
from dataset import CustomDataset, get_default_transform


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="My Diffusion Model Trainer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--n-steps",
        type=int,
        default=500,
        help="Number of steps to run the simulation.",
    )
    parser.add_argument(
        "--beta1",
        type=float,
        default=1e-4,
        help="Beta1 parameter for the model.",
    )
    parser.add_argument(
        "--beta2",
        type=float,
        default=0.02,
        help="Beta2 parameter for the model.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda:0",
        help="Device to use for the simulation.",
    )
    parser.add_argument(
        "--n-feat",
        type=int,
        default=64,
        help="Number of features in the model.",
    )
    parser.add_argument(
        "--n-c-feat",
        type=int,
        default=5,
        help="Number of features in the context model.",
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=128,
        help="Batch size for the simulation.",
    )
    parser.add_argument(
        "--lr",
        type=float,
        default=1e-3,
        help="Learning rate for the simulation.",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=32,
        help="Number of epochs to train the model.",
    )
    parser.add_argument(
        "--save",
        type=str,
        default="./weights/",
        help="Path to save the model weights.",
    )
    return parser.parse_args()


def perturb_input(
    x: torch.Tensor, ab_t: torch.Tensor, t: torch.Tensor, noise: torch.Tensor
):
    """Perturb the input image using the DDPM noise schedule.

    Args:
        x: The input image. (b, c, h, w)
        ab_t: The DDPM noise schedule. (n_steps + 1, )
        t: The time step to perturb the image. (b, )
        noise: The noise to add to the image. (b, c, h, w)
    """
    return (
        ab_t.sqrt()[t, None, None, None] * x + (1 - ab_t[t, None, None, None]) * noise
    )


if __name__ == "__main__":
    args = get_args()
    if args.device == "mps" and not torch.backends.mps.is_available():
        args.device = "cpu"
    elif args.device.startswith("cuda") and not torch.cuda.is_available():
        args.device = "cpu"

    device = torch.device(args.device)
    print(device)

    # construct DDPM noise schedule
    b_t = (args.beta2 - args.beta1) * torch.linspace(
        0, 1, args.n_steps + 1, device=args.device
    ) + args.beta1
    a_t = 1 - b_t
    ab_t = torch.cumsum(a_t.log(), dim=0).exp()
    ab_t[0] = 1

    # Load the dataset
    dataset = CustomDataset(
        "./sprites_1788_16x16.npy",
        "./sprite_labels_nc_1788_16x16.npy",
        get_default_transform(),
        null_context=False,
    )
    dataloader = DataLoader(
        dataset, batch_size=args.batch, shuffle=True, num_workers=4, pin_memory=True
    )

    # construct Model
    nn_model = ContextUnet(
        in_channels=3, n_feat=args.n_feat, n_cfeat=args.n_c_feat, height=16
    ).to(device)

    # Training
    optim = torch.optim.Adam(nn_model.parameters(), lr=args.lr)
    nn_model.train()
    best_mse = float("inf")
    for epoch in range(args.epochs):
        print("Epoch:", epoch)

        optim.param_groups[0]["lr"] = args.lr * (1 - epoch / args.epochs)
        pbar = tqdm(dataloader, total=len(dataloader))

        mses = []

        for x, context in pbar:
            optim.zero_grad()
            x = x.to(device)
            context = context.to(x)

            # randomly mask out context
            context_mask = torch.bernoulli(torch.zeros(context.shape[0]) + 0.9).to(
                device
            )
            context = context * context_mask.unsqueeze(-1)

            noise = torch.randn_like(x)
            t_step = torch.randint(1, args.n_steps, (x.shape[0],)).to(device)
            noise = torch.randn_like(x)
            x_perturbed = perturb_input(x, ab_t, t_step, noise)

            pred_noise = nn_model(x_perturbed, t_step / args.n_steps, c=context)

            loss = F.mse_loss(pred_noise, noise)
            loss.backward()

            optim.step()

            mses.append(loss.item())
            pbar.set_description(f"Mean Loss: {torch.mean(torch.Tensor(mses)):.4f}")


        mean_mse = torch.mean(torch.Tensor(mses))

        if mean_mse < best_mse:
            best_mse = mean_mse
            torch.save(
                nn_model.state_dict(),
                os.path.join(args.save, "best_model.pt"),
            )
            print(f"Best Model saved at {os.path.join(args.save, 'best_model.pt')}")

        if (epoch % 4) == 0 or (epoch == args.epochs - 1):
            model_path = os.path.join(args.save, f"model_epoch_{epoch}.pt")
            torch.save(
                nn_model.state_dict(),
                model_path,
            )
            print(f"Model saved at {model_path}")
