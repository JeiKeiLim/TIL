import argparse
import os
import time

import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.nn.functional as F

from model import ContextUnet

from typing import Tuple, Optional, List


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="My Diffusion Model Inference",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda:0",
        help="Device to use for the simulation.",
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
        "--model",
        type=str,
        default="./weights/best_model.pt",
        help="Path to the model weights.",
    )
    return parser.parse_args()


class Denoiser:
    def __init__(
        self,
        model: ContextUnet,
        n_steps: int,
        beta1: float,
        beta2: float,
        device: torch.device,
    ) -> None:
        """

        Args:
            model: Model to use for denoising
            n_steps: Number of steps to run the simulation (ddpm)
            beta1: Beta1 parameter for the denoising schedule
            beta2: Beta2 parameter for the denoising schedule
            device: Device to use for the simulation
        """
        self.model = model
        self.n_steps = n_steps
        self.beta1 = beta1
        self.beta2 = beta2

        self.b_t = (beta2 - beta1) * torch.linspace(
            0, 1, n_steps + 1, device=device
        ) + beta1
        self.a_t = 1 - b_t
        self.ab_t = torch.cumsum(a_t.log(), dim=0).exp()
        self.ab_t[0] = 1

    @torch.no_grad()
    def denoise_add_noise(
        self,
        x: torch.Tensor,
        pred_noise: torch.Tensor,
        t_step: int,
        z=Optional[torch.Tensor],
    ) -> torch.Tensor:
        """Denoise the image and add noise for the next timestep

        Args:
            x: Image tensor (B, C, H, W)
            pred_noise: Predicted noise tensor
            t_step: Current timestep
            z: Noise tensor (B, C, H, W) if None, generate new noise

        Returns:
            Denoised image tensor
        """
        if z is None:
            z = torch.randn_like(x)
        noise = self.b_t.sqrt()[t_step] * z
        mean = (
            x - pred_noise * ((1 - self.a_t[t_step]) / (1 - self.ab_t[t_step]).sqrt())
        ) / self.a_t[t_step].sqrt()
        return mean + noise

    @torch.no_grad()
    def sample_ddpm_context(
        self,
        n_sample: int,
        context: torch.Tensor,
        save_rate: int = 20,
        target_shape: Tuple[int, int] = (16, 16),
    ) -> Tuple[torch.Tensor, np.ndarray]:
        """

        Args:
            model: Model to use for sampling
            n_sample: Number of samples to generate
            context: Context tensor
            timesteps: Number of timesteps to run the simulation
            save_rate: Save rate for intermediate samples for animated visualization
            target_shape: Shape of the target image
        """
        # x_T ~ N(0, 1), sample initial noise
        samples = torch.randn(n_sample, 3, target_shape[0], target_shape[1]).to(device)

        # array to keep track of generated steps for plotting
        intermediate = []
        for i in range(self.n_steps, 0, -1):
            print(f"sampling timestep {i:3d}", end="\r")

            # reshape time tensor
            t = torch.tensor([i / self.n_steps])[:, None, None, None].to(device)

            # sample some random noise to inject back in. For i = 1, don't add back in noise
            if i > 1:
                z = torch.randn_like(samples)
            else:
                z = torch.zeros_like(samples)

            pred_noise = self.model(
                samples, t, c=context
            )  # predict noise e_(x_t,t, ctx)
            samples = self.denoise_add_noise(samples, pred_noise, i, z)
            if i % save_rate == 0 or i == self.n_steps or i < 8:
                intermediate.append(samples.detach().cpu().numpy())

        intermediate = np.stack(intermediate)
        return samples, intermediate

    @torch.no_grad()
    def denoise_ddim(
        self, x: torch.Tensor, t_step: int, t_step_prev: int, pred_noise: torch.Tensor
    ) -> torch.Tensor:
        """Denoise the image using the DDIM noise schedule

        Args:
            x: Image tensor (B, C, H, W)
            t_step: Current timestep
            t_step_prev: Previous timestep
            pred_noise: Predicted noise tensor

        Returns:
            Denoised image tensor
        """
        ab = self.ab_t[t_step]
        ab_prev = self.ab_t[t_step_prev]

        x0_pred = ab_prev.sqrt() / ab.sqrt() * (x - (1 - ab).sqrt() * pred_noise)
        dir_xt = (1 - ab_prev).sqrt() * pred_noise

        return x0_pred + dir_xt

    @torch.no_grad()
    def sample_ddim_context(
        self,
        n_sample: int,
        context: torch.Tensor,
        n_skip: int = 20,
        target_shape: Tuple[int, int] = (16, 16),
    ) -> Tuple[torch.Tensor, np.ndarray]:
        """Sample using the DDIM noise schedule

        Args:
            n_sample: Number of samples to generate
            context: Context tensor
            n_skip: Number of steps to skip for intermediate samples
            target_shape: Shape of the target

        Returns:
            Generated samples and intermediate
        """
        # x_T ~ N(0, 1), sample initial noise
        samples = torch.randn(n_sample, 3, target_shape[0], target_shape[1]).to(device)

        # array to keep track of generated steps for plotting
        intermediate = []
        step_size = self.n_steps // n_skip
        for i in range(self.n_steps, 0, -step_size):
            print(f"sampling timestep {i:3d}", end="\r")

            # reshape time tensor
            t = torch.tensor([i / self.n_steps])[:, None, None, None].to(device)

            pred_noise = nn_model(samples, t, c=context)  # predict noise e_(x_t,t)
            samples = self.denoise_ddim(samples, i, i - step_size, pred_noise)
            intermediate.append(samples.detach().cpu().numpy())

        intermediate = np.stack(intermediate)
        return samples, intermediate


def show_images(
    imgs: torch.Tensor, nrow: int = 2, labels: Optional[List[str]] = None
) -> None:
    """Show images in a grid

    Args:
        imgs: Image tensor to show
        nrow: Number of rows to show
        labels: List of labels for the images
    """
    _, axs = plt.subplots(nrow, imgs.shape[0] // nrow, figsize=(4, 2))
    axs = axs.flatten()
    for i, (img, ax) in enumerate(zip(imgs, axs)):
        img = (img.permute(1, 2, 0).clip(-1, 1).detach().cpu().numpy() + 1) / 2
        ax.set_xticks([])
        ax.set_yticks([])

        if labels is not None:
            ax.set_title(labels[i])
        ax.imshow(img)
    plt.show()


if __name__ == "__main__":
    args = get_args()

    if args.device == "mps" and not torch.backends.mps.is_available():
        args.device = "cpu"
    elif args.device.startswith("cuda") and not torch.cuda.is_available():
        args.device = "cpu"

    device = torch.device(args.device)

    # construct DDPM noise schedule
    b_t = (args.beta2 - args.beta1) * torch.linspace(
        0, 1, args.n_steps + 1, device=args.device
    ) + args.beta1
    a_t = 1 - b_t
    ab_t = torch.cumsum(a_t.log(), dim=0).exp()
    ab_t[0] = 1

    # construct Model
    nn_model = ContextUnet(
        in_channels=3, n_feat=args.n_feat, n_cfeat=args.n_c_feat, height=16
    ).to(device)

    nn_model.load_state_dict(torch.load(args.model, map_location=device))

    denoiser = Denoiser(nn_model, args.n_steps, args.beta1, args.beta2, device)

    # hero, non-hero, food, spell, side-facing
    labels = np.array(("hero", "non-hero", "food", "spell", "side-facing"))

    context = F.one_hot(torch.randint(0, 5, (8,)), 5).to(device=device).float()
    ctx_labels = labels[torch.argmax(context, dim=1).cpu().numpy()].tolist()

    t0_ddpm = time.time_ns()
    samples_ddpm, _ = denoiser.sample_ddpm_context(
        context.shape[0],
        context,
        save_rate=20,
        target_shape=(16, 16),
    )
    t1_ddpm = time.time_ns()

    t0_ddim = time.time_ns()
    samples_ddim, _ = denoiser.sample_ddim_context(
        context.shape[0],
        context,
        n_skip=20,
        target_shape=(16, 16),
    )
    t1_ddim = time.time_ns()

    samples_ddpm_ddim = torch.cat([samples_ddpm, samples_ddim], dim=0)
    ctx_labels = ctx_labels + ctx_labels

    print(f"DDPM Time: {(t1_ddpm - t0_ddpm) / 1e6:,.2f} ms")
    print(f"DDIM Time: {(t1_ddim - t0_ddim) / 1e6:,.2f} ms")

    show_images(samples_ddpm_ddim, labels=ctx_labels, nrow=4)

    # mix of defined context
    context = (
        torch.tensor(
            [
                # hero, non-hero, food, spell, side-facing
                [1, 0, 0, 0, 0],  # human
                [1, 0, 0.6, 0, 0],
                [0, 0, 0.6, 0.4, 0],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 1, 0],
            ]
        )
        .float()
        .to(device)
    )
    t0_ddpm = time.time_ns()
    samples_ddpm, _ = denoiser.sample_ddpm_context(
        context.shape[0],
        context,
        save_rate=20,
        target_shape=(16, 16),
    )
    t1_ddpm = time.time_ns()

    t0_ddim = time.time_ns()
    samples_ddim, _ = denoiser.sample_ddim_context(
        context.shape[0],
        context,
        n_skip=20,
        target_shape=(16, 16),
    )
    t1_ddim = time.time_ns()

    print(f"DDPM Time: {(t1_ddpm - t0_ddpm) / 1e6:,.2f} ms")
    print(f"DDIM Time: {(t1_ddim - t0_ddim) / 1e6:,.2f} ms")

    samples_ddpm_ddim = torch.cat([samples_ddpm, samples_ddim], dim=0)
    show_images(samples_ddpm_ddim, nrow=4)
