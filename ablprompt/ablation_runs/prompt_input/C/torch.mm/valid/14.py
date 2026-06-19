import torch

# Create two random 2D tensors
a = torch.randn(5, 3)
b = torch.randn(3, 4)

# Perform matrix multiplication
result = torch.mm(a, b)

print(result)