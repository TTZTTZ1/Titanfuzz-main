import torch

# Create a tensor of random values
base_tensor = torch.randn(3, 4)

# Create an exponent tensor of ones
exponent_tensor = torch.ones(3, 4)

# Compute element-wise exponentiation
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)