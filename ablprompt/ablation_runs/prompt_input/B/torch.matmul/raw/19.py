import torch

# Create random tensors
a = torch.randn(3, 4)
b = torch.randn(4, 2)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)