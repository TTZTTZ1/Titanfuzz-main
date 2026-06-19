import torch

# Define the EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum')

# Create random input tensor and offsets
input = torch.randint(0, 10, (8,), dtype=torch.long)  # Random indices between 0 and 9
offsets = torch.tensor([0, 4, 8], dtype=torch.long)  # Offsets for two bags

# Compute the embedding bag
output = embedding_bag(input, offsets)

print(output)