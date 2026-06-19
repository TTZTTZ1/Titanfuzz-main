import torch
from torch.nn.functional import grid_sample

# Create a random input tensor of shape (1, 1, 28, 28)
input_tensor = torch.randn(1, 1, 28, 28)

# Create a grid tensor of shape (1, 28, 28, 2) with normalized coordinates
grid_tensor = torch.rand(1, 28, 28, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Should print: torch.Size([1, 1, 28, 28])