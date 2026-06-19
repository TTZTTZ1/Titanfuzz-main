import torch

# Create a random tensor and an exponent tensor
base_tensor = torch.randn(3, 4)
exponent_tensor = torch.tensor([2, 3])

# Compute element-wise power using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)