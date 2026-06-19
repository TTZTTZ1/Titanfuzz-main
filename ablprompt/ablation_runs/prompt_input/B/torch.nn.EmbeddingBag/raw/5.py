import torch
import torch.nn as nn

# Define an EmbeddingBag layer
embedding_bag = nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum', sparse=True)

# Create some input data and offsets
input_data = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
offsets = torch.LongTensor([0, 4])

# Compute the embedding bag
output = embedding_bag(input_data, offsets)

print(output)