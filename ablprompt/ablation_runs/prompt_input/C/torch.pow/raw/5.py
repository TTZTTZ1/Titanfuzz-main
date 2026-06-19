import torch

# Create a tensor and an exponent tensor
base_tensor = torch.tensor([1, 2, 3, 4])
exponent_tensor = torch.tensor([2, 3, 4, 5])

# Compute element-wise power using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)