import torch

# Prepare valid input data
tensor = torch.randn(3, 5)
sparsity = 0.5
std = 0.1
generator = torch.Generator().manual_seed(42)

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)