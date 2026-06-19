import torch

# Create two random 3D tensors
batch_size = 2
n = 3
m = 4
p = 5
input_tensor = torch.randn(batch_size, n, m)
mat2_tensor = torch.randn(batch_size, m, p)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result)