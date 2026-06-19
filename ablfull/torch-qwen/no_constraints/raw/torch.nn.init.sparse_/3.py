import torch

# Prepare input data
tensor = torch.zeros(5, 5)
sparsity = 0.7
std = 0.01

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std)