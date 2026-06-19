import torch

# Create a random tensor
a = torch.randn(3, 4)

# Create an exponent tensor
b = torch.tensor([2, 3])

# Compute element-wise power
result = torch.pow(a, b)

print(result)