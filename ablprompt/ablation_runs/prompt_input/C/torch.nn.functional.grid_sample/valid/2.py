import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 1, 32, 32)
input_tensor = torch.randn(1, 1, 32, 32)

# Create a grid of shape (1, 32, 32, 2) with normalized coordinates
grid = torch.rand(1, 32, 32, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 1, 32, 32])