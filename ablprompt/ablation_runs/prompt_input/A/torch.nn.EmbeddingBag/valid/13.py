import torch

# Define parameters for EmbeddingBag
embedding_dim = 10
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'mean'
sparse = False
padding_idx = -1

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings=100, embedding_dim=embedding_dim,
                                      max_norm=max_norm, norm_type=norm_type,
                                      scale_grad_by_freq=scale_grad_by_freq, mode=mode,
                                      sparse=sparse, padding_idx=padding_idx)

# Example input: indices and offsets
indices = torch.tensor([3, 4, 7])
offsets = torch.tensor([0, 2])

# Call the EmbeddingBag
output = embedding_bag(indices, offsets)
print(output)