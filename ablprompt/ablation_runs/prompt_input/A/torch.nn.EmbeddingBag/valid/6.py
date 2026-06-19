import torch

# Define the embedding bag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3)

# Sample input indices and offsets
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Forward pass through the embedding bag layer
output = embedding_bag(indices, offsets)

print(output)