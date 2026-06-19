import torch

# Define parameters for EmbeddingBag
embedding_dim = 10
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'mean'
sparse = False

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(embedding_dim, max_norm=max_norm, norm_type=norm_type,
                                       scale_grad_by_freq=scale_grad_by_freq, mode=mode, sparse=sparse)

# Prepare input data
indices = torch.tensor([1, 2, 4, 5])
offsets = torch.tensor([0, 2])

# Forward pass through the embedding bag layer
output = embedding_bag(indices, offsets)

print(output)