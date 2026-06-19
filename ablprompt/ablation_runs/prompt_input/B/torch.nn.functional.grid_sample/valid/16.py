import torch
from torch.nn.functional import grid_sample, affine_grid

# Create a random input tensor
batch_size = 1
channels = 3
height_in = 64
width_in = 64
input_tensor = torch.randn(batch_size, channels, height_in, width_in)

# Define an affine transformation matrix
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transform

# Generate a grid based on the affine transformation
grid = affine_grid(theta, size=(batch_size, channels, height_in, width_in))

# Apply grid sample
output_tensor = grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)