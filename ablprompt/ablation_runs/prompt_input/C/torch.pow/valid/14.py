import torch

# Create a tensor
base_tensor = torch.tensor([2, 3, 4])

# Create an exponent tensor
exponent_tensor = torch.tensor([0, 1, 2])

# Compute element-wise exponentiation
result = torch.pow(base_tensor, exponent_tensor)

print(result)