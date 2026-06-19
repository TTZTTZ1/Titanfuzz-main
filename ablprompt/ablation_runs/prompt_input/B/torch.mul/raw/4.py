import torch

# Create two tensors
a = torch.randn(3, 4, 5)
b = torch.randn(4, 5)

# Perform element-wise multiplication
result = torch.mul(a, b)

print(result)