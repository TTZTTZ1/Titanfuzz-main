import torch

# Create random tensors for demonstration
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)