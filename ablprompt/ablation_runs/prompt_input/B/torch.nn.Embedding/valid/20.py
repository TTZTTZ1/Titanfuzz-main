import torch
import torch.nn as nn

# Create an embedding layer with 10 embeddings of size 3
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Example input tensor of indices
input_indices = torch.LongTensor([[1, 2], [3, 4]])

# Get the corresponding embedding vectors
output_embeddings = embedding(input_indices)

print(output_embeddings)