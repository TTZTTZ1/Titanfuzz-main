import torch

# Define the EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='mean', sparse=True)

# Create random input tensor and offsets
input = torch.randint(0, 10, (10,))
offsets = torch.tensor([0, 4, 10])

# Compute the embedding bag
output = embedding_bag(input, offsets)

print(output)