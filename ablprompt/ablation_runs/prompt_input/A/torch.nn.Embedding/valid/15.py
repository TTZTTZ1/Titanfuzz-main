import torch
from torch import nn

# Define an embedding layer with 10 tokens and an embedding dimension of 5
embedding_layer = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Example input: a tensor of token indices [2, 4, 1]
input_indices = torch.tensor([2, 4, 1])

# Get the embeddings for the input indices
embeddings = embedding_layer(input_indices)

print(embeddings)