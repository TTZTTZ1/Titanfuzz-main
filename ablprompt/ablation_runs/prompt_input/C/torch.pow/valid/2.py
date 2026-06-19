import torch

# Create a tensor and a scalar
base_tensor = torch.tensor([2.0, 3.0, 4.0])
exponent_scalar = 3

# Compute element-wise exponentiation
result = torch.pow(base_tensor, exponent_scalar)

print(result)