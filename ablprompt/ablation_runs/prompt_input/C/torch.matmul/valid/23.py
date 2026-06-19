import torch

# Create two random tensors with compatible shapes for batched matrix multiplication
batch_size = 3
m = 2
n = 3
k = 4

a = torch.randn(batch_size, m, n)
b = torch.randn(batch_size, n, k)

# Perform batched matrix multiplication using torch.matmul
result = torch.matmul(a, b)

print(result)