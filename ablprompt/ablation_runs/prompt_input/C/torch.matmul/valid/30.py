import torch

# Create two random tensors of compatible shapes
a = torch.randn(3, 4)
b = torch.randn(4, 2)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)