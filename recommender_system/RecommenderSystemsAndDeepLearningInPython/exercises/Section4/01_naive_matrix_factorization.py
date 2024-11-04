import os, sys, inspect

import numpy as np

from tqdm import tqdm

# Add parent directory to path for importing modules
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # type: ignore
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from utils.dataset_loader import MovieLens20MDatasetLoader


if __name__ == "__main__":
    path = "~/Datasets/MovieLens20M/rating.csv"

    dataset = MovieLens20MDatasetLoader(path, subset_ratio=1.0)
    train_set, test_set = dataset.get_train_test_split(test_size=0.001, shuffle_set=False)

    K = 10
    EPOCHS = 25

    unique_train_users = train_set.data["userId"].unique()
    unique_train_items = train_set.data["movieId"].unique()

    global_item_bias = np.mean(train_set.data["rating"].values)  # type: ignore

    # Initialize user and item latent factors
    W = np.random.randn(dataset.user_ids.shape[0], K)
    U = np.random.randn(dataset.item_ids.shape[0], K)

    # WARNING: This takes about 13.8 GB of memory
    rating_matrix = np.zeros(
        (dataset.user_ids.shape[0], dataset.item_ids.shape[0]), dtype=np.float32
    )
    rating_matrix[train_set.data["userId"].values, train_set.data["movieId"].values] = (
        train_set.data["rating"].values
    )

    bias_user = np.zeros(dataset.user_ids.shape[0])
    bias_item = np.zeros(dataset.item_ids.shape[0])

    regularization = 20.

    n_items_by_user = dataset.data.groupby("userId").size()
    n_users_by_item = dataset.data.groupby("movieId").size()

    item_ids_by_user = dataset.data.groupby("userId")["movieId"].apply(list)
    user_ids_by_item = dataset.data.groupby("movieId")["userId"].apply(list)

    for epoch in tqdm(range(EPOCHS), desc="Training"):
        for i in tqdm(dataset.user_ids, desc="Solving W"):
            # with bias and regularization
            m_ids = item_ids_by_user[i]

            W[i] = np.linalg.solve(
                np.dot(U[m_ids].T, U[m_ids]) + regularization * np.eye(K),
                np.dot(
                    U[m_ids].T,
                    rating_matrix[i, m_ids]
                    - bias_item[m_ids]
                    - global_item_bias
                    - bias_user[i],
                ),
            )

            bias_user[i] = np.sum(
                rating_matrix[i, m_ids]
                - np.dot(U[m_ids], W[i])
                - global_item_bias
                - bias_item[m_ids]
            ) / (regularization + n_items_by_user[i])

        for j in tqdm(dataset.item_ids, desc="Solving U"):
            # with bias and regularization
            u_ids = user_ids_by_item[j]

            U[j] = np.linalg.solve(
                np.dot(W[u_ids].T, W[u_ids]) + regularization * np.eye(K),
                np.dot(
                    W[u_ids].T,
                    rating_matrix[u_ids, j]
                    - bias_user[u_ids]
                    - global_item_bias
                    - bias_item[j],
                ),
            )

            bias_item[j] = np.sum(
                rating_matrix[u_ids, j]
                - np.dot(W[u_ids], U[j])
                - global_item_bias
                - bias_user[u_ids]
            ) / (regularization + n_users_by_item[j])

        # Predict ratings for the train set
        test_user_ids = train_set.data["userId"].values
        test_item_ids = train_set.data["movieId"].values
        test_ratings = train_set.data["rating"].values

        predictions = np.zeros(test_ratings.shape[0])
        for i in tqdm(range(test_ratings.shape[0]), desc="Predicting on train set"):
            # With bias
            predictions[i] = (
                np.dot(W[test_user_ids[i]], U[test_item_ids[i]])
                + global_item_bias
                + bias_user[test_user_ids[i]]
                + bias_item[test_item_ids[i]]
            )

        predictions = np.clip(predictions, 0.5, 5.0)

        # Calculate RMSE
        rmse_train = np.sqrt(np.mean((test_ratings - predictions) ** 2))  # type: ignore

        # Predict ratings for the test set
        test_user_ids = test_set.data["userId"].values
        test_item_ids = test_set.data["movieId"].values
        test_ratings = test_set.data["rating"].values

        predictions = np.zeros(test_ratings.shape[0])
        for i in tqdm(range(test_ratings.shape[0]), desc="Predicting on test set"):
            predictions[i] = (
                np.dot(W[test_user_ids[i]], U[test_item_ids[i]])
                + global_item_bias
                + bias_user[test_user_ids[i]]
                + bias_item[test_item_ids[i]]
            )

        predictions = np.clip(predictions, 0.5, 5.0)

        # Calculate RMSE
        rmse_test = np.sqrt(np.mean((test_ratings - predictions) ** 2))  # type: ignore
        print(f"Epoch: {epoch}, RMSE(Train): {rmse_train}, RMSE_Test: {rmse_test}")
