import torch

# Create random tensors with varying dimensions
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.randn(6, 7, 8)

# Perform batched matrix multiplication
result = torch.matmul(c, torch.matmul(a, b))

print(result)