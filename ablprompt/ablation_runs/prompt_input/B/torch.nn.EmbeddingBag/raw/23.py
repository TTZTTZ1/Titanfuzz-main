import torch
import torch.nn as nn

# Define the EmbeddingBag layer
embedding_bag = nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum', sparse=True)

# Create input tensors
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2]])
offsets = torch.LongTensor([0, 4])

# Compute the embedding bag
output = embedding_bag(input, offsets)

print(output)