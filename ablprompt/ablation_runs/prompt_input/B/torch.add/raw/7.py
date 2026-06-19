import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.randn(3, 4)
b = torch.randn(4)

# Perform element-wise addition with scaling
result = torch.add(a, b, alpha=2)

print(result)