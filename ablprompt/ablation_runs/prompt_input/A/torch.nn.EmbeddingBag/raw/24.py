import torch

# Define parameters for EmbeddingBag
num_embeddings = 10
embedding_dim = 3
max_norm = None
norm_type = 2.0
scale_grad_by_freq = False
mode = 'sum'
sparse = False

# Create an instance of EmbeddingBag
embedding_bag = torch.nn.EmbeddingBag(num_embeddings, embedding_dim, max_norm=max_norm, norm_type=norm_type, scale_grad_by_freq=scale_grad_by_freq, mode=mode, sparse=sparse)

# Prepare input data
indices = torch.tensor([[4, 5, 7], [0, 2, 8]])
offsets = torch.tensor([0, 3])

# Call the EmbeddingBag
output = embedding_bag(indices, offsets)

print(output)