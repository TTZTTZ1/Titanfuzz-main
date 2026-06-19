import torch

# Create random tensors with compatible shapes for batched matrix multiplication
batch_size = 3
rows = 4
cols = 5
a = torch.randn(batch_size, rows, cols)
b = torch.randn(batch_size, cols, 6)

# Perform batched matrix multiplication
result = torch.matmul(a, b)

print(result)