import torch

# Create an EmbeddingBag layer
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=5, embedding_dim=3, mode='sum', padding_idx=0)

# Define input indices and offsets
input_indices = torch.tensor([[1, 2, 4], [4, 3, 2]], dtype=torch.long)
offsets = torch.tensor([0, 3], dtype=torch.long)

# Compute the embedding bag
output = embedding_bag(input_indices, offsets)

print(output)