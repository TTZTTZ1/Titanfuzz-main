import torch

# Create two random 3D tensors with compatible shapes
input_tensor = torch.randn(5, 3, 4)
mat2_tensor = torch.randn(5, 4, 6)

# Perform batch matrix-matrix multiplication
result = torch.bmm(input_tensor, mat2_tensor)

print(result.shape)  # Should print: torch.Size([5, 3, 6])