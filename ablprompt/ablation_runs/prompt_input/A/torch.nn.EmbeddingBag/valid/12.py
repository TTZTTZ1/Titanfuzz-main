import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=10, embedding_dim=3)

# Prepare some input data
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Call the EmbeddingBag layer
output = embedding_bag(indices, offsets)

print(output)