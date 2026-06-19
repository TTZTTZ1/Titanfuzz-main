import torch
from torch.nn.functional import grid_sample

# Create a random input tensor of shape (1, 1, 64, 64)
input_tensor = torch.randn(1, 1, 64, 64)

# Create a grid of shape (1, 64, 64, 2) with normalized coordinates
grid = torch.rand(1, 64, 64, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Should print torch.Size([1, 1, 64, 64])