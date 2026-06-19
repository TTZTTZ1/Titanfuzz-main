import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Create an exponent tensor
exponent_tensor = torch.tensor([2, 3])

# Compute element-wise power using torch.pow
result_tensor = torch.pow(input_tensor, exponent_tensor)

print(result_tensor)