import torch

# Create two random 3D tensors
input_tensor = torch.randn(5, 3, 4)
mat2_tensor = torch.randn(5, 4, 2)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Expected shape: (5, 3, 2)