import torch

# Create a random tensor and an exponent tensor
input_tensor = torch.randn(3, 4)
exponent_tensor = torch.tensor([2, 3])

# Perform element-wise exponentiation
result = torch.pow(input_tensor, exponent_tensor)

print(result)