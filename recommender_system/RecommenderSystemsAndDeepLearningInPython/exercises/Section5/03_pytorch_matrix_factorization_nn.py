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
    def __init__(self, n_users: int, n_items: int, K: int, n_hidden: int) -> None:
        super().__init__()

        self.W = nn.Embedding(n_users, K)
        self.U = nn.Embedding(n_items, K)
        self.hidden1 = nn.Linear(K * 2, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, 1)

    def forward(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
        w = self.W(user_ids)
        u = self.U(item_ids)

        h = torch.cat([w, u], dim=1)

        hidden_out = self.hidden2(self.hidden1(h)).squeeze()

        return torch.clip(hidden_out, 0.5, 5.0)


if __name__ == "__main__":
    path = "~/Datasets/MovieLens20M/rating.csv"

    dataset = MovieLens20MDatasetLoader(path, subset_ratio=1.0)
    train_set, test_set = dataset.get_train_test_split(
        test_size=0.001, shuffle_set=False
    )

    K = 10
    EPOCHS = 1000
    LR = 0.01
    batch_size = 10240 * 5

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = Model(dataset.user_ids.shape[0], dataset.item_ids.shape[0], K, 16).to(
        device
    )

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

    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    loss_fn = nn.MSELoss()

    p_bar = tqdm(range(EPOCHS), desc="Training")
    for epoch in p_bar:
        train_losses = []
        for i in range(0, len(train_user_ids), batch_size):
            batch_user_ids = train_user_ids[i : i + batch_size]
            batch_item_ids = train_item_ids[i : i + batch_size]
            batch_ratings = train_ratings[i : i + batch_size]

            prediction = model(batch_user_ids, batch_item_ids)

            loss = loss_fn(prediction, batch_ratings)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_losses.append([loss.item()])

        test_losses = []
        with torch.no_grad():
            for i in range(0, len(test_user_ids), batch_size):
                batch_user_ids = test_user_ids[i : i + batch_size]
                batch_item_ids = test_item_ids[i : i + batch_size]
                batch_ratings = test_ratings[i : i + batch_size]

                prediction = model(batch_user_ids, batch_item_ids)
                loss = loss_fn(prediction, batch_ratings)

                test_losses.append([loss.item()])

        p_bar.set_postfix(
            {"Loss(Train)": np.mean(train_losses), "Loss(Test)": np.mean(test_losses)}
        )
