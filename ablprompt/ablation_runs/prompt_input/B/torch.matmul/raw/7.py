import torch

# Create two random tensors with compatible shapes for batched matrix multiplication
batch_size = 3
m = 4
n = 5
k = 6
a = torch.randn(batch_size, m, n)
b = torch.randn(batch_size, n, k)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)