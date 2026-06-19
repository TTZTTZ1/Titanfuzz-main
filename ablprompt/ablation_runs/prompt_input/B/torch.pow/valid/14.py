import torch

# Create two tensors of different shapes
base = torch.tensor([[1, 2], [3, 4]])
exponent = torch.tensor([2, 3])

# Compute element-wise power using torch.pow
result = torch.pow(base, exponent)

print(result)