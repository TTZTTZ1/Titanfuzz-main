import torch

# Define parameters for the EmbeddingBag layer
num_embeddings = 100
embedding_dim = 32
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'mean'
sparse = False
padding_idx = -1

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=max_norm, norm_type=norm_type,
                                      scale_grad_by_freq=scale_grad_by_freq, mode=mode, sparse=sparse,
                                      padding_idx=padding_idx)

# Example input: indices and offsets
indices = torch.tensor([1, 2, 4, 5], dtype=torch.long)
offsets = torch.tensor([0, 2, 4], dtype=torch.long)

# Generate random embeddings
embeddings = torch.randn(num_embeddings, embedding_dim)

# Call the EmbeddingBag layer
output = embedding_bag(embeddings, offsets)

print(output)