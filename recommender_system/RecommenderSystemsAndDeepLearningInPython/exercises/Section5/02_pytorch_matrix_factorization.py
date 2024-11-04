import os, sys, inspect

import numpy as np

from tqdm import tqdm
import torch
import torch.nn as nn

# Add parent directory to path for importing modules
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # type: ignore
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.dataset_loader import MovieLens20MDatasetLoader


class Model(nn.Module):
    def __init__(self, n_users: int, n_items: int, K: int, global_mean: float) -> None:
        super().__init__()

        self.W = nn.Embedding(n_users, K)
        self.U = nn.Embedding(n_items, K)

        self.bias_user = nn.Parameter(torch.zeros(n_users, dtype=torch.float32))
        self.bias_item = nn.Parameter(
            torch.zeros(n_items, requires_grad=True, dtype=torch.float32)
        )
        self.global_mean = nn.Parameter(
            torch.tensor(global_mean, dtype=torch.float32), requires_grad=False
        )

    def forward(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
        wu = torch.einsum("ij, ij -> i", self.W(user_ids), self.U(item_ids))
        return (
            self.bias_user[user_ids] + self.bias_item[item_ids] + self.global_mean + wu
        )


if __name__ == "__main__":
    path = "~/Datasets/MovieLens20M/rating.csv"

    dataset = MovieLens20MDatasetLoader(path, subset_ratio=1.0)
    train_set, test_set = dataset.get_train_test_split(
        test_size=0.001, shuffle_set=False
    )

    K = 10
    EPOCHS = 1000
    LR = 100.0

    global_item_bias = np.mean(train_set.data["rating"].values)  # type: ignore

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = Model(
        dataset.user_ids.shape[0], dataset.item_ids.shape[0], K, global_item_bias
    ).to(device)

    train_user_ids = torch.tensor(train_set.data["userId"].values, device=device)
    train_item_ids = torch.tensor(train_set.data["movieId"].values, device=device)
    train_ratings = torch.tensor(
        train_set.data["rating"].values, device=device, dtype=torch.float32
    )
    test_user_ids = torch.tensor(test_set.data["userId"].values, device=device)
    test_item_ids = torch.tensor(test_set.data["movieId"].values, device=device)
    test_ratings = torch.tensor(
        test_set.data["rating"].values, device=device, dtype=torch.float32
    )

    optimizer = torch.optim.SGD(model.parameters(), lr=LR)
    loss_fn = nn.MSELoss()

    p_bar = tqdm(range(EPOCHS), desc="Training")
    for epoch in p_bar:
        prediction = model(train_user_ids, train_item_ids)

        train_loss = loss_fn(prediction, train_ratings)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        with torch.no_grad():
            prediction = model(test_user_ids, test_item_ids)
            test_loss = loss_fn(prediction, test_ratings)

        p_bar.set_postfix(
            {"Loss(Train)": train_loss.item(), "Loss(Test)": test_loss.item()}
        )

