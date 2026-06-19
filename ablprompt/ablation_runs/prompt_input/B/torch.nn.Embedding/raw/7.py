import torch
import torch.nn as nn

# Define the embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Create input indices
input_indices = torch.LongTensor([[1, 2], [3, 4]])

# Get the embeddings
embeddings = embedding(input_indices)

print(embeddings)