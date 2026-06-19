import torch

# Prepare valid input data
tensor = torch.zeros(4, 4)
sparsity = 0.5

# Call the API
result = torch.nn.init.sparse_(tensor, sparsity)