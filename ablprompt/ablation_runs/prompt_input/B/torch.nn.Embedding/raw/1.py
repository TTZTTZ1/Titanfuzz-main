import torch
import torch.nn as nn

# Create an Embedding layer with 5 unique tokens and each token having an embedding dimension of 8
embedding = nn.Embedding(num_embeddings=5, embedding_dim=8)

# Example input: LongTensor of shape (3, 2), representing indices of tokens
input_indices = torch.LongTensor([[1, 2], [0, 3], [4, 1]])

# Get the embeddings for the input indices
embeddings = embedding(input_indices)

print(embeddings.shape)  # Expected output shape: (3, 2, 8)