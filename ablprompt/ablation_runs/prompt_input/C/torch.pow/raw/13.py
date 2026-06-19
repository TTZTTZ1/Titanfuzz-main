import torch

# Create a random tensor
base_tensor = torch.randn(3, 4)

# Create an exponent tensor
exponent_tensor = torch.tensor([2, 3])

# Compute element-wise power
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)