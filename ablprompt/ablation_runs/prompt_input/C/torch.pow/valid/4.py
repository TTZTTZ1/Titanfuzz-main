import torch

# Create a tensor and an exponent tensor
base_tensor = torch.tensor([2, 3, 4])
exponent_tensor = torch.tensor([3, 2, 1])

# Compute element-wise exponentiation using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)