import torch

# Create two tensors
base = torch.tensor([2.0, 3.0, 4.0])
exponent = torch.tensor([3.0])

# Compute element-wise power using torch.pow
result = torch.pow(base, exponent)

print(result)