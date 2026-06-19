import torch
import torch.nn as nn

# Define an embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create some input indices
input_indices = torch.LongTensor([1, 2, 4, 5])

# Get the embeddings for the input indices
embeddings = embedding(input_indices)

print(embeddings)