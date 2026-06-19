import torch

# Create a random tensor
base = torch.randn(3, 4)

# Create an exponent tensor
exponent = torch.tensor([2, 3])

# Compute power using torch.pow
result = torch.pow(base, exponent)

print(result)