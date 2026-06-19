import torch
import torch.nn as nn

# Create an embedding layer with 5 unique tokens and each token represented by a 3-dimensional vector
embedding_layer = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Example input: a batch of two sequences, where each sequence has three tokens
input_indices = torch.tensor([[1, 2, 4], [0, 3, 2]])

# Get the embeddings for the given input indices
embeddings = embedding_layer(input_indices)

print(embeddings)