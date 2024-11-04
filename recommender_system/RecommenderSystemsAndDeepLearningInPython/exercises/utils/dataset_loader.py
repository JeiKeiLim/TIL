import pandas as pd
import numpy as np

from typing import Tuple, Union, List


class MovieLens20MDatasetLoader:
    def __init__(self, path: str, subset_ratio: float = 1.0) -> None:
        """Load the MovieLens 20M dataset from the given path.

        Args:
            path: Path to the dataset csv file (rating.csv)
            subset_ratio: Ratio of the dataset to load. Defaults to 1.0.
        """
        self.path = path
        print(f"Loading dataset from {path}...")
        self.data = pd.read_csv(path)

        if subset_ratio < 1.0:
            self.data = self.data.sample(frac=subset_ratio, random_state=42)

        print(f"Dataset loaded. Shape: {self.data.shape}")

        user_ids = np.array(self.data["userId"].unique())
        item_ids = np.array(self.data["movieId"].unique())

        # Reindexing user and item IDs to start from 0 and increment by 1
        item_id_map = {item_id: idx for idx, item_id in enumerate(item_ids)}
        user_id_map = {user_id: idx for idx, user_id in enumerate(user_ids)}

        self.data["movie_idx"] = self.data["movieId"].copy()

        self.data["userId"] = self.data["userId"].apply(lambda val: user_id_map[val])
        self.data["movieId"] = self.data["movieId"].apply(
            lambda val: item_id_map[val]
        )

        self.user_ids = np.array(self.data["userId"].unique())
        self.item_ids = np.array(self.data["movieId"].unique())

    def get_train_test_split(
        self, test_size: float = 0.2, shuffle_set: bool = False
    ) -> Tuple["MovieLens20MDataset", "MovieLens20MDataset"]:
        """Split the dataset into train and test sets.

        Split the dataset is based on the user IDs.

        Args:
            test_size: Ratio of the dataset to be used for testing.
            shuffle_set: Whether to shuffle the dataset before splitting.
        """
        user_ids = self.user_ids.copy()
        if shuffle_set:
            np.random.shuffle(user_ids)

        n_train_ids = int(len(user_ids) * (1 - test_size))
        train_ids = user_ids[:n_train_ids]
        test_ids = user_ids[n_train_ids:]

        train_data = self.data[self.data["userId"].isin(train_ids)]  # type: ignore
        test_data = self.data[self.data["userId"].isin(test_ids)]  # type: ignore

        return MovieLens20MDataset(train_data), MovieLens20MDataset(test_data)  # type: ignore


class MovieLens20MDataset:
    def __init__(self, data: pd.DataFrame) -> None:
        """Initialize the dataset with the given data.

        Args:
            data: DataFrame containing the dataset.
        """
        self.data = data
        self.user_ids = data["userId"].unique()
        self.item_ids = data["movieId"].unique()

    def get_user_data(self, user_id: int) -> pd.DataFrame:
        """Get the data for the given user ID.

        Args:
            user_id: ID of the user.
        """
        return self.data[self.data["userId"] == user_id]  # type: ignore

    def get_item_data(self, item_ids: Union[int, List]) -> pd.DataFrame:
        """Get the data for the given item IDs.

        Args:
            item_ids: ID of the item(s).
                If a list is provided, data for all the items will be returned.
        """
        if isinstance(item_ids, int):
            item_ids = [item_ids]

        return self.data.query(f"movieId in {item_ids}")  # type: ignore


if __name__ == "__main__":
    path = "~/Datasets/MovieLens20M/rating.csv"

    dataset = MovieLens20MDatasetLoader(path)
    train_set, test_set = dataset.get_train_test_split(test_size=0.2, shuffle_set=True)
    data = train_set.get_user_data(train_set.user_ids[0])
    __import__("pdb").set_trace()
