import torch
import torch.nn as nn

# Create an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create input indices
input_indices = torch.LongTensor([1, 2, 3])

# Get embeddings for the input indices
embeddings = embedding(input_indices)

print(embeddings)