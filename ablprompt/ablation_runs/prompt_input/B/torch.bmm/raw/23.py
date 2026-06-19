import torch

# Create two random 3D tensors with batch size 2, each having dimensions 3x4 and 4x5 respectively
input_tensor = torch.randn(2, 3, 4)
mat2_tensor = torch.randn(2, 4, 5)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result)