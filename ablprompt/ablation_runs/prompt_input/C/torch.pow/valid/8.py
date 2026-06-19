import torch

# Create a tensor
a = torch.tensor([1, 2, 3])

# Create an exponent tensor
b = torch.tensor([2, 3, 4])

# Compute element-wise exponentiation
result = torch.pow(a, b)

print(result)