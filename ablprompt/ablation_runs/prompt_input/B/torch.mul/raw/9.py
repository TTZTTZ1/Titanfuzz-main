import torch

# Create two tensors with different shapes
a = torch.randn(2, 3, 4)
b = torch.randn(4)

# Perform element-wise multiplication with broadcasting
result = torch.mul(a, b)

print(result)