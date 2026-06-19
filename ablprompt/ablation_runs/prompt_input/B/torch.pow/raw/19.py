import torch

# Create two tensors
base = torch.tensor([2.0, 3.0, 4.0])
exponent = torch.tensor([3, 2])

# Compute element-wise exponentiation
result = torch.pow(base, exponent)

print(result)