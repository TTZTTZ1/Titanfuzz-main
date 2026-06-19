import torch

# Define parameters for the EmbeddingBag layer
embedding_dim = 10
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'sum'
sparse = False
padding_idx = -1

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=100, embedding_dim=embedding_dim, max_norm=max_norm, norm_type=norm_type, scale_grad_by_freq=scale_grad_by_freq, mode=mode, sparse=sparse, padding_idx=padding_idx)

# Example input tensor (batch of indices)
indices = torch.tensor([[4, 5, 6], [7, 8, 9]])

# Example offsets tensor (start and end indices for each sequence in the batch)
offsets = torch.tensor([0, 3])

# Call the EmbeddingBag layer
output = embedding_bag(indices, offsets)

print(output)