import torch
import torch.nn as nn

# Define the EmbeddingBag layer
embedding_bag = nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum')

# Create random input tensor
input = torch.randint(0, 10, (8,), dtype=torch.long)

# Create offsets tensor for variable-length bags
offsets = torch.tensor([0, 4], dtype=torch.long)

# Compute the embedding bag
output = embedding_bag(input, offsets)

print(output)