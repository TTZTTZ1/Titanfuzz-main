import torch
import torch.nn as nn

# Create an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=5)

# Example input tensor of indices
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings
embeddings = embedding(input_indices)

print(embeddings)