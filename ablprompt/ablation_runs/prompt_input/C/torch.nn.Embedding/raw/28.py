import torch
import torch.nn as nn

# Create an Embedding layer
embedding = nn.Embedding(num_embeddings=10, embedding_dim=3)

# Prepare input data
input_data = torch.LongTensor([1, 2, 3, 4])

# Get embeddings for the input data
output = embedding(input_data)

print(output)