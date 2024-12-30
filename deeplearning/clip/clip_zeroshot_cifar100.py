"""This script requres to install clip
pip install git+https://github.com/openai/CLIP.git
"""

import os
import clip
import torch
from torchvision.datasets import CIFAR100
from torch.utils.data import DataLoader
from tqdm import tqdm

from typing import Tuple


def get_features(dataset: Dataset) -> Tuple[torch.Tensor, torch.Tensor]:
    all_features = []
    all_labels = []

    with torch.no_grad():
        for images, labels in tqdm(DataLoader(dataset, batch_size=100)):
            features = model.encode_image(images.to(device))

            all_features.append(features)
            all_labels.append(labels)

    return torch.cat(all_features), torch.cat(all_labels)


if __name__ == "__main__":
    device = "mps"
    model, preprocess = clip.load("ViT-B/32", device=device)

    root = os.path.expanduser("~/.cache")
    train = CIFAR100(root, download=True, train=True, transform=preprocess)
    test = CIFAR100(root, download=True, train=False, transform=preprocess)

    text_inputs = torch.cat(
        [clip.tokenize(f"a photo of a {c}") for c in train.classes]
    ).to(device)
    text_features = model.encode_text(text_inputs)
    text_features /= text_features.norm(dim=-1, keepdim=True)

    # Calculate the image features
    train_features, train_labels = get_features(train)
    test_features, test_labels = get_features(test)

    train_features /= train_features.norm(dim=-1, keepdim=True)
    test_features /= test_features.norm(dim=-1, keepdim=True)

    train_similarities = (100.0 * train_features @ text_features.T).softmax(dim=-1)
    test_similarities = (100.0 * test_features @ text_features.T).softmax(dim=-1)

    train_predictions = train_similarities.argmax(dim=-1)
    test_predictions = test_similarities.argmax(dim=-1)

    train_labels = train_labels.to(device)
    test_labels = test_labels.to(device)

    train_accuracy = train_predictions.eq(train_labels).float().mean().item()
    test_accuracy = test_predictions.eq(test_labels).float().mean().item()

    print(f"Train accuracy: {train_accuracy:.1%}")
    print(f"Test accuracy: {test_accuracy:.1%}")
