import torch
import torch.nn as nn

# Create an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Create input tensor with indices
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embedded vectors
embedded_vectors = embedding(input_indices)

print(embedded_vectors)