import torch
import torch.nn as nn

# Create an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Example input tensor of indices
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embedded vectors
embedded_vectors = embedding(input_indices)

print(embedded_vectors)