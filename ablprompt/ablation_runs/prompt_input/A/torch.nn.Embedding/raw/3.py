import torch
import torch.nn as nn

# Define an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some input indices
indices = torch.LongTensor([4, 2, 9])

# Get the embeddings for the input indices
embedded_indices = embedding(indices)

print(embedded_indices)