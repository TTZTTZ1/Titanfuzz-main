import torch
import torch.nn as nn

# Define the EmbeddingBag layer
embedding_bag = nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum')

# Create some input data and offsets
input_data = torch.tensor([[1, 2, 4, 5], [4, 3, 2, 9]], dtype=torch.long)
offsets = torch.tensor([0, 4], dtype=torch.long)

# Compute the output
output = embedding_bag(input_data, offsets)

print(output)