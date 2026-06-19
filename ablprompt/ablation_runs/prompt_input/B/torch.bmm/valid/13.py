import torch

# Create two random 3D tensors with compatible shapes
input_tensor = torch.randn(10, 3, 4)
mat2_tensor = torch.randn(10, 4, 5)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Expected output: torch.Size([10, 3, 5])