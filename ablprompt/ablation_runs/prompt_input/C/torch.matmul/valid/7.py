import torch

# Create two random tensors for batched matrix multiplication
batch_size = 2
m = 3
n = 4
k = 5
a = torch.randn(batch_size, m, n)
b = torch.randn(batch_size, n, k)

# Perform batched matrix multiplication using torch.matmul
c = torch.matmul(a, b)

print(c)