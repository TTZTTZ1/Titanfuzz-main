import torch

# Create two random tensors with compatible shapes for batched matrix multiplication
batch_size = 2
m, n, p = 3, 4, 5
a = torch.randn(batch_size, m, n)
b = torch.randn(batch_size, n, p)

# Perform batched matrix multiplication using torch.matmul
result = torch.matmul(a, b)

print(result)