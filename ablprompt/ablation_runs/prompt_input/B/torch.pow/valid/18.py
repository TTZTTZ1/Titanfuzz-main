import torch

# Create a random tensor and an exponent tensor
base = torch.randn(3, 4)
exponent = torch.randint(0, 5, (3, 4))

# Compute element-wise exponentiation
result = torch.pow(base, exponent)

print(result)