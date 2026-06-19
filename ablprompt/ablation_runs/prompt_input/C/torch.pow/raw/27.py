import torch

# Create a random tensor
base_tensor = torch.randn(3, 4)

# Define an exponent as a scalar
exponent_scalar = 2

# Compute element-wise power using torch.pow
result_tensor = torch.pow(base_tensor, exponent_scalar)

print(result_tensor)