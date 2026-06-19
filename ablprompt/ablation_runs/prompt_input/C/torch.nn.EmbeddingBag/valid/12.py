import torch

# Define the EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='sum')

# Create random input tensor and offsets
input = torch.randint(0, 10, (8,), dtype=torch.long)
offsets = torch.tensor([0, 4, 8], dtype=torch.long)

# Compute the output
output = embedding_bag(input, offsets)

print(output)