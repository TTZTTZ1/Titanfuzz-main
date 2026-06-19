import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 1, 10, 10)
input_tensor = torch.randn(1, 1, 10, 10)

# Create a grid of shape (1, 10, 10, 2) with values in [-1, 1]
grid = torch.rand(1, 10, 10, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and no padding
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor)