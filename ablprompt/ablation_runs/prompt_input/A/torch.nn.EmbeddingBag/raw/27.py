import torch

# Define the embedding bag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3)

# Create some input data: indices of embeddings to use and offsets for bags
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Forward pass through the embedding bag layer
output = embedding_bag(indices, offsets)

print(output)