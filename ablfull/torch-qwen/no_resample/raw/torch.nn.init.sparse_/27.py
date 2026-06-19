import torch

# Prepare valid input data
tensor = torch.zeros(3, 3)
sparsity = 0.5
std = 0.1

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std=std)