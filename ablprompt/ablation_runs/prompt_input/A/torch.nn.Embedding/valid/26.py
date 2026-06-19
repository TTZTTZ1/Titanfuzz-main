import torch
import torch.nn as nn

# Define an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some input indices
indices = torch.tensor([1, 2, 4, 5])

# Get embeddings for these indices
embedded_indices = embedding(indices)

print(embedded_indices)