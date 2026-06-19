import torch

# Create two tensors
base = torch.tensor([[1, 2], [3, 4]])
exponent = torch.tensor([[0, 1], [2, 3]])

# Compute element-wise exponentiation
result = torch.pow(base, exponent)

print(result)