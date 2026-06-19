import torch

# Prepare valid input data
tensor = torch.zeros((5, 5))
sparsity = 0.2
std = 0.1
generator = torch.Generator().manual_seed(0)

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)