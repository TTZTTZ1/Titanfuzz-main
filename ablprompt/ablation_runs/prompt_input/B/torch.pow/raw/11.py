import torch

# Create random tensors
a = torch.randn(3, 4)
b = torch.randn(4)

# Perform element-wise exponentiation using torch.pow
result = torch.pow(a, b)

print(result)