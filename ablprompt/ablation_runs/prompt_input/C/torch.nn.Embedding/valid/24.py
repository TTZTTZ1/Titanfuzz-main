import torch
import torch.nn as nn

# Create an Embedding layer with 5 unique tokens and each token having an embedding dimension of 3
embedding_layer = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Example input: a batch of two sequences, each sequence has three tokens
input_indices = torch.LongTensor([[1, 2, 4], [0, 3, 2]])

# Get the embeddings for the given input indices
embeddings = embedding_layer(input_indices)

print(embeddings)