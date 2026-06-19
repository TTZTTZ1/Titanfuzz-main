import torch

# Define parameters for EmbeddingBag
embedding_dim = 10
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'mean'
sparse = False

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=100, embedding_dim=embedding_dim, max_norm=max_norm, norm_type=norm_type, scale_grad_by_freq=scale_grad_by_freq, mode=mode, sparse=sparse)

# Example input tensors
indices = torch.tensor([1, 2, 4, 5])
weights = torch.tensor([1.0, 2.0, 3.0, 4.0])
offsets = torch.tensor([0, 2])

# Call the EmbeddingBag
output = embedding_bag(indices, offsets, weights)
print(output)