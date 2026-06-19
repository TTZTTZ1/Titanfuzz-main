import torch
import torch.nn as nn

# Create an embedding layer with 5 embeddings of size 3
embedding = nn.Embedding(num_embeddings=5, embedding_dim=3)

# Define input indices
input_indices = torch.LongTensor([0, 1, 2, 3, 4])

# Get the embeddings for the input indices
embeddings = embedding(input_indices)

print(embeddings)