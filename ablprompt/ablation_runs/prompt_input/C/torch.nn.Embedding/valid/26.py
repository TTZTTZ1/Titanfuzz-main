import torch
import torch.nn as nn

# Define the Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Create some input indices
indices = torch.tensor([1, 2, 4, 5])

# Get the embedded vectors
embedded_vectors = embedding(indices)

print(embedded_vectors)