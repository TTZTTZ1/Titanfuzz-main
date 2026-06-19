import torch

# Create two random 3D tensors with compatible shapes for batch matrix multiplication
input_tensor = torch.randn(10, 3, 4)
mat2_tensor = torch.randn(10, 4, 5)

# Perform batch matrix multiplication using torch.bmm
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Expected output shape: (10, 3, 5)