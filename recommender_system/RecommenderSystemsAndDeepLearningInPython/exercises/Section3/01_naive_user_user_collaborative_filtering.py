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
    train_set, test_set = dataset.get_train_test_split(
        test_size=0.001, shuffle_set=False
    )

    print("Calculating mean ratings by user ...")
    train_mean_ratings_by_user = train_set.data.groupby("userId")["rating"].mean()
    test_mean_ratings_by_user = test_set.data.groupby("userId")["rating"].mean()

    print("Calculating deviations ...")
    train_set.data["deviation"] = train_set.data.apply(
        lambda x: x["rating"] - train_mean_ratings_by_user[x["userId"]], axis=1
    )
    test_set.data["deviation"] = test_set.data.apply(
        lambda x: x["rating"] - test_mean_ratings_by_user[x["userId"]], axis=1
    )

    TOP_K = 30
    MIN_OVERLAP = 5

    # Computing user-user similarity
    mean_erros = []
    for test_user_id in tqdm(test_set.user_ids):
        data = test_set.get_user_data(test_user_id)
        test_user_mean_rating = test_mean_ratings_by_user[test_user_id]

        union_item_ids = np.intersect1d(data["movieId"], train_set.item_ids)  # type: ignore

        union_train_data = train_set.get_item_data(union_item_ids.tolist())
        union_train_user_ids = union_train_data["userId"].unique()

        # weights = [[id, 0.0] for id in union_train_user_ids]
        weights = []
        for i, user_id in tqdm(
            enumerate(union_train_user_ids),
            desc="Calculating weights",
            total=len(union_train_user_ids),
        ):
            user_data = union_train_data[union_train_data["userId"] == user_id]

            user_rating_deviations: np.ndarray = user_data["deviation"].values  # type: ignore

            if user_rating_deviations.size < MIN_OVERLAP:
                continue

            test_rating_deviations: np.ndarray = data[  # type: ignore
                data["movieId"].isin(user_data["movieId"])  # type: ignore
            ][
                "deviation"
            ].values  # type: ignore

            weight = np.dot(user_rating_deviations, test_rating_deviations) / (
                np.linalg.norm(user_rating_deviations)
                * np.linalg.norm(test_rating_deviations)
                + 1e-9
            )

            weights.append([user_id, weight])

            weights.sort(key=lambda x: x[1], reverse=True)
            # ratio = pow((i + 1) / len(union_train_user_ids), 10)

            if len(weights) > TOP_K:
                weights = weights[:TOP_K]
                #
                # if weights[-1][1] > (1 - ratio):
                #     break

        weights = weights[: min(TOP_K, len(weights))]

        errors = []
        # Predicting ratings
        for _, row in data.iterrows():
            item_id = row["movieId"]

            weighted_rating_deviations = []
            sum_weights = sum([abs(weight) for _, weight in weights])
            for user_id, weight in weights:
                user_data = train_set.get_user_data(user_id)
                user_data = user_data.query(f"movieId == {item_id}")

                if user_data.empty:
                    sum_weights -= abs(weight)
                    continue

                weighted_rating_deviation = weight * user_data["deviation"]
                weighted_rating_deviations.append(weighted_rating_deviation.values[0])

            if sum_weights == 0:
                predicted_rating = test_user_mean_rating
            else:
                predicted_rating = (
                    test_user_mean_rating
                    + sum(weighted_rating_deviations) / sum_weights
                )

            predicted_rating = np.clip(predicted_rating, 0.5, 5.0)
            squared_error = (row["rating"] - predicted_rating) ** 2
            errors.append(squared_error)

            print(
                f"    User ID: {test_user_id}, Item ID: {item_id}, Predicted vs Actual Ratings: {predicted_rating:.2f} vs {row['rating']:.2f}, Difference: {np.sqrt(squared_error):.2f}"
            )

        print(
            f"User ID: {test_user_id}, RMSE: {np.sqrt(np.mean(errors)):.2f}, MAE: {np.mean(errors):.2f}"
        )
        mean_erros.append(np.mean(errors))

    print(f"Mean RMSE: {np.mean(mean_erros):.2f}")
