import torch

# Define an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3)

# Create some input data: indices and offsets
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Call the EmbeddingBag layer
output = embedding_bag(indices, offsets)

print(output)