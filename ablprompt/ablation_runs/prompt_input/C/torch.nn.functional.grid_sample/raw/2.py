import torch
from torch.nn.functional import grid_sample

# Create a random input tensor of shape (1, 1, 4, 4)
input_tensor = torch.randn(1, 1, 4, 4)

# Create a grid tensor of shape (1, 4, 4, 2) with values in [-1, 1]
grid_tensor = torch.rand(1, 4, 4, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor)