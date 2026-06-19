import torch

# Prepare valid input data
a = torch.tensor([1, 2])
b = torch.tensor([3.5, 4.5])

# Call the target API
result = torch.cartesian_prod(a, b)