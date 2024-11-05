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
    def __init__(self, n_items: int, n_hidden: int) -> None:
        super().__init__()
        self.layer1 = nn.Linear(n_items, n_hidden)
        self.activation = nn.Tanh()
        self.layer2 = nn.Linear(n_hidden, n_items)
        self.dropout = nn.Dropout(0.7)

    def forward(self, x: torch.Tensor, is_train: bool = False) -> torch.Tensor:
        if is_train:
            out = self.dropout(x)
        else:
            out = x

        out = self.layer1(out)
        out = self.activation(out)
        out = self.layer2(out)

        return out


if __name__ == "__main__":
    path = "~/Datasets/MovieLens20M/rating.csv"

    dataset = MovieLens20MDatasetLoader(path, subset_ratio=1.0)
    train_set, test_set = dataset.get_train_test_split(
        test_size=0.001, shuffle_set=False
    )

    EPOCHS = 1000
    LR = 0.1
    batch_size = 10240 * 2

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = Model(dataset.item_ids.shape[0], 512).to(device)

    # WARNING: This takes about 13.8*2 GB of memory
    rating_matrix = np.zeros(
        (dataset.user_ids.shape[0], dataset.item_ids.shape[0]), dtype=np.float32
    )
    rating_matrix[train_set.data["userId"].values, train_set.data["movieId"].values] = (
        train_set.data["rating"].values
    )
    rating_matrix[test_set.data["userId"].values, test_set.data["movieId"].values] = (
        test_set.data["rating"].values
    )
    rating_matrix = torch.tensor(rating_matrix, dtype=torch.float32, device="cpu")
    rating_mask = rating_matrix != 0

    unique_train_user_ids = train_set.data["userId"].unique()
    unique_test_user_ids = test_set.data["userId"].unique()

    mean_train_rating = torch.tensor(
        train_set.data["rating"].mean(), device=device, dtype=torch.float32
    )

    optimizer = torch.optim.SGD(model.parameters(), lr=LR, momentum=0.9)
    loss_fn = nn.MSELoss()

    p_bar = tqdm(range(EPOCHS), desc="Training")
    for epoch in p_bar:
        train_losses = []
        for i in range(0, unique_train_user_ids.shape[0], batch_size):
            mat = rating_matrix[unique_train_user_ids[i : i + batch_size]].to(device)  # type: ignore
            mask = rating_mask[unique_train_user_ids[i : i + batch_size]].to(device)  # type: ignore
            mat[mask] -= mean_train_rating

            prediction = model(mat, is_train=True)

            loss = loss_fn(prediction[mask], mat[mask])

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_losses.append([loss.item()])

        test_losses = []
        with torch.no_grad():
            for i in range(0, unique_test_user_ids.shape[0], batch_size):
                mat = rating_matrix[unique_test_user_ids[i : i + batch_size]].to(device)  # type: ignore
                mask = rating_mask[unique_test_user_ids[i : i + batch_size]].to(device)  # type: ignore
                mat[mask] -= mean_train_rating

                prediction = model(mat, is_train=True)

                loss = loss_fn(prediction[mask], mat[mask])

                test_losses.append([loss.item()])

        p_bar.set_postfix(
            {"Loss(Train)": np.mean(train_losses), "Loss(Test)": np.mean(test_losses)}
        )

    test_losses = []
    with torch.no_grad():
        for i in range(0, unique_test_user_ids.shape[0], batch_size):
            mat = rating_matrix[unique_test_user_ids[i : i + batch_size]].to(device)  # type: ignore
            mask = rating_mask[unique_test_user_ids[i : i + batch_size]].to(device)  # type: ignore
            mat[mask] -= mean_train_rating

            prediction = model(mat, is_train=False)

            loss = loss_fn(prediction[mask], mat[mask])

            test_losses.append([loss.item()])

    print(f"Final Test Loss: {np.mean(test_losses)}, RMSE: {np.sqrt(np.mean(test_losses))}")
