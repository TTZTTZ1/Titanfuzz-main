import torch

# Create a random tensor and an exponent tensor
base = torch.randn(3, 4)
exponent = torch.tensor([2, 3])

# Perform element-wise exponentiation
result = torch.pow(base, exponent)

print(result)