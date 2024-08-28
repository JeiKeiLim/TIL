import torch
import torch.nn as nn
from torch.nn import functional as F

from torchtext.transforms import BERTTokenizer
import torchtext
from tqdm import tqdm


class SelfAttention(nn.Module):
    def __init__(self, embed_size: int) -> None:
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.queries = nn.Linear(embed_size, embed_size)
        self.keys = nn.Linear(embed_size, embed_size)
        self.values = nn.Linear(embed_size, embed_size)
        self.divisor = torch.sqrt(torch.tensor(self.embed_size, dtype=torch.float32))

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
    ) -> torch.Tensor:
        query = self.queries(query)
        key = self.keys(key)
        value = self.values(value)

        attention = torch.matmul(query, key.transpose(-2, -1)) / self.divisor
        attention = F.softmax(attention, dim=-1)

        out = torch.matmul(attention, value)

        return out


if __name__ == "__main__":
    VOCAB_FILE = "https://huggingface.co/bert-base-uncased/resolve/main/vocab.txt"
    tokenizer = BERTTokenizer(
        vocab_path=VOCAB_FILE, do_lower_case=True, return_tokens=True
    )

    text = "Hello, my dog is cute"
    tokens = tokenizer(text)

    glove = torchtext.vocab.GloVe(name="840B", dim=300)
    embeddings = glove.get_vecs_by_tokens(tokens)
    embeddings = embeddings.unsqueeze(0)

    attention = SelfAttention(300)

    optimizer = torch.optim.Adam(attention.parameters(), lr=0.001)

    with tqdm(range(100)) as pbar:
        for step in pbar:
            optimizer.zero_grad()
            out = attention(embeddings, embeddings, embeddings)

            loss = (embeddings - out).pow(2).sum([1, 2]).mean()

            loss.backward()
            optimizer.step()
            pbar.set_description(f"Loss: {loss.item()}")
    out = attention(embeddings, embeddings, embeddings)
    __import__('pdb').set_trace()
