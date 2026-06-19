import torch

# Create random tensors for input and mat2
batch_size = 5
n = 3
m = 4
p = 2
input_tensor = torch.randn(batch_size, n, m)
mat2_tensor = torch.randn(batch_size, m, p)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Expected shape: (5, 3, 2)