import torch

# Create two tensors of different shapes
a = torch.randn(3, 4)
b = torch.randn(4)

# Perform element-wise subtraction with broadcasting
result = torch.sub(a, b, alpha=2)

print(result)