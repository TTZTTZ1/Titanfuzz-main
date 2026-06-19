import torch

# Create two random 3D tensors with compatible shapes for batch matrix multiplication
batch_size = 10
n = 3
m = 4
p = 5

input_tensor = torch.randn(batch_size, n, m)
mat2_tensor = torch.randn(batch_size, m, p)

# Perform batch matrix multiplication using torch.bmm
result_tensor = torch.bmm(input_tensor, mat2_tensor)

print(result_tensor.shape)  # Expected output shape: (10, 3, 5)