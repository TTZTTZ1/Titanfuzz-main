import torch
import torch.nn as nn

# Define the embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Create input indices
input_indices = torch.tensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(input_indices)

print(embeddings)