import torch

# Create a tensor of random values
a = torch.randn(3, 4)

# Create a scalar exponent
b = 2

# Compute element-wise exponentiation
result = torch.pow(a, b)

print(result)