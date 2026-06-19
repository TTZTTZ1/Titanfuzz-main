import torch

# Create some random tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)