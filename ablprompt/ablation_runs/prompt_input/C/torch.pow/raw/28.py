import torch

# Create a tensor and an exponent tensor
base_tensor = torch.tensor([2.0, 3.0, 4.0])
exponent_tensor = torch.tensor([3, 2])

# Compute element-wise exponentiation
result = torch.pow(base_tensor, exponent_tensor)

print(result)