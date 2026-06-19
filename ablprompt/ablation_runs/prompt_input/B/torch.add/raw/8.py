import torch

# Create two tensors of different shapes
a = torch.randn(3, 4)
b = torch.randn(4)

# Use torch.add with broadcasting
result = torch.add(a, b, alpha=2)

print(result)