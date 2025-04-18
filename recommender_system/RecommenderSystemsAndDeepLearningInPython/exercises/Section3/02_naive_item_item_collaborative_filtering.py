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

    print("Calculating mean ratings by item ...")
    train_mean_item_ratings = train_set.data.groupby("movieId")["rating"].mean()
    test_mean_item_ratings = test_set.data.groupby("movieId")["rating"].mean()

    print("Calculating deviations ...")
    train_set.data["deviation"] = train_set.data.apply(
        lambda x: x["rating"] - train_mean_item_ratings[x["movieId"]], axis=1
    )
    test_set.data["deviation"] = test_set.data.apply(
        lambda x: x["rating"] - test_mean_item_ratings[x["movieId"]], axis=1
    )

    unique_test_user_ids = test_set.data["userId"].unique()
    weights = {}

    TOP_K = 30
    MIN_OVERLAP = 5
    mean_erros = []
    for test_user_id in tqdm(
        unique_test_user_ids,
        total=unique_test_user_ids.shape[0],
        desc="Calculating weights",
    ):
        test_user_data = test_set.get_user_data(test_user_id)
        test_item_ids = test_user_data["movieId"].unique().tolist()

        train_user_data = train_set.get_item_data(test_item_ids)

        for target_item_id in tqdm(test_item_ids, total=len(test_item_ids), desc=""):
            target_item_data = train_user_data.query(f"movieId == {target_item_id}")

            # Calculate weights
            for train_item_id in test_item_ids:
                if target_item_id == train_item_id:
                    continue
                if (target_item_id, train_item_id) in weights:
                    continue

                train_item_data = train_user_data.query(f"movieId == {train_item_id}")

                common_user_id = np.intersect1d(
                    target_item_data["userId"], train_item_data["userId"]
                )
                common_user_id = np.unique(common_user_id).tolist()

                if len(common_user_id) < MIN_OVERLAP:
                    continue

                common_item_data_i = target_item_data.query(
                    f"userId in {common_user_id}"
                ).sort_values(
                    by="userId"
                )  # type: ignore
                common_item_data_j = train_item_data.query(
                    f"userId in {common_user_id}"
                ).sort_values(
                    by="userId"
                )  # type: ignore

                numerator = np.dot(
                    common_item_data_i["deviation"], common_item_data_j["deviation"]
                )

                denominator = np.linalg.norm(
                    common_item_data_i["deviation"]
                ) * np.linalg.norm(common_item_data_j["deviation"])

                weight = numerator / (denominator + 1e-9)

                weights[(target_item_id, train_item_id)] = weight
                weights[(train_item_id, target_item_id)] = weight

        errors = []
        for target_item_id in test_item_ids:
            target_item_data = train_user_data.query(f"movieId == {target_item_id}")
            # Sort weights
            sorted_weights = []
            for train_item_id in test_item_ids:
                if target_item_id == train_item_id:
                    continue

                if (target_item_id, train_item_id) not in weights:
                    continue

                sorted_weights.append(
                    (train_item_id, weights[(target_item_id, train_item_id)])
                )

                sorted_weights.sort(key=lambda x: x[1], reverse=True)

                if len(sorted_weights) > TOP_K:
                    sorted_weights = sorted_weights[:TOP_K]

            # Calculate prediction
            numerator = 0
            sum_weights = sum([abs(weight) for _, weight in sorted_weights])
            for train_item_id, weight in sorted_weights:
                test_deviation = test_user_data.query(f"movieId == {train_item_id}")[
                    "deviation"
                ].values[0]

                numerator += weight * test_deviation

            if target_item_id not in train_mean_item_ratings:
                continue

            if sum_weights == 0:
                prediction = train_mean_item_ratings[target_item_id]
            else:
                prediction = (
                    train_mean_item_ratings[target_item_id] + numerator / sum_weights
                )
            prediction = np.clip(prediction, 0.5, 5.0)

            answer = test_user_data.query(f"movieId == {target_item_id}")[
                "rating"
            ].values[0]
            squared_error = (prediction - answer) ** 2
            errors.append(squared_error)

            print(
                f"    User ID: {test_user_id}, Item ID: {target_item_id}, Predicted vs Actual Ratings: {prediction:.2f} vs {answer:.2f}, Difference: {np.sqrt(squared_error):.2f}"
            )
        print(
            f"User ID: {test_user_id}, RMSE: {np.sqrt(np.mean(errors)):.2f}, MAE: {np.mean(errors):.2f}"
        )
        mean_erros.append(np.mean(errors))

    print(f"Mean RMSE: {np.mean(mean_erros):.2f}")
