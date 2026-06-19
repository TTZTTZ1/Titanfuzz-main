import torch

# Create two random 3D tensors with shapes (2, 3, 4) and (2, 4, 5)
input_tensor = torch.randn(2, 3, 4)
mat2_tensor = torch.randn(2, 4, 5)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Expected output shape: (2, 3, 5)