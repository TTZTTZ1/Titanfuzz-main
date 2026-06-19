import torch

# Create two tensors of different shapes
a = torch.randn(2, 3, 4)
b = torch.randn(3, 4)

# Perform element-wise multiplication using torch.mul
result = torch.mul(a, b)

print(result)