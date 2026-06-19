import torch

# Define parameters for the EmbeddingBag layer
num_embeddings = 10
embedding_dim = 3

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings, embedding_dim)

# Sample input data: indices and offsets
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Forward pass through the EmbeddingBag layer
output = embedding_bag(indices, offsets)

print(output)