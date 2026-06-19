import torch

# Create a tensor
base_tensor = torch.tensor([1, 2, 3, 4])

# Create an exponent tensor
exponent_tensor = torch.tensor([2, 3, 0.5, -1])

# Compute element-wise power using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)