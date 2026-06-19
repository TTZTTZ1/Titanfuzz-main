import torch
import torch.nn as nn

# Define the embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Create input tensor with indices
input_indices = torch.LongTensor([[1, 2], [3, 4]])

# Get the embedded vectors
embedded_vectors = embedding(input_indices)

print(embedded_vectors)