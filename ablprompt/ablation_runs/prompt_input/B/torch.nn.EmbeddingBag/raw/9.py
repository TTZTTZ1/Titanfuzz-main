import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum', sparse=True)

# Define input tensor (fixed-length bags)
input = torch.tensor([[1, 2, 4, 5], [4, 3, 2]], dtype=torch.long)

# Compute embeddings
output = embedding_bag(input)

print(output)