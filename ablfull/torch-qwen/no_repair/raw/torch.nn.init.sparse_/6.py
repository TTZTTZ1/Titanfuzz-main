import torch

# Prepare input data
tensor = torch.randn(5, 5)
sparsity = 0.2
std = 0.1
generator = torch.Generator().manual_seed(42)

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)