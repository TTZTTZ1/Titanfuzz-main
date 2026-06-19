import torch

# Create two tensors with different shapes
base = torch.tensor([[1, 2], [3, 4]])
exponent = torch.tensor([2])

# Perform element-wise exponentiation using torch.pow
result = torch.pow(base, exponent)

print(result)