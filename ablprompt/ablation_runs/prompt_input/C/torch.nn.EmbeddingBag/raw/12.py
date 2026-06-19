import torch

# Define the EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3, mode='mean', sparse=True)

# Create some random input data
input_data = torch.randint(0, 10, (8,), dtype=torch.long)

# Create offsets for variable-length bags
offsets = torch.tensor([0, 4, 8], dtype=torch.long)

# Compute the embedding bag
output = embedding_bag(input_data, offsets)

print(output)