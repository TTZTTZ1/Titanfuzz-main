import torch

# Create a random tensor and an exponent tensor
base_tensor = torch.randn(3, 4)
exponent_tensor = torch.randint(0, 5, (3, 4))

# Compute element-wise exponentiation using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)