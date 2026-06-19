import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum', sparse=True)

# Define input indices and offsets
input_indices = torch.tensor([1, 2, 4, 5, 4, 3, 2, 9], dtype=torch.long)
offsets = torch.tensor([0, 4], dtype=torch.long)

# Compute the embedding bag
output = embedding_bag(input_indices, offsets)

print(output)