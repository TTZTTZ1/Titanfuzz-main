import torch
from torch.nn.functional import grid_sample, affine_grid

# Create a random input tensor and an affine transformation matrix
batch_size = 1
channels = 3
height_in = width_in = 64
theta = torch.tensor([[[1.0, 0.0, 32], [0.0, 1.0, 32]]])  # Translation by (32, 32)
grid = affine_grid(theta, (batch_size, channels, height_in, width_in))

# Generate a random input tensor
input_tensor = torch.randn(batch_size, channels, height_in, width_in)

# Apply grid sample
output_tensor = grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)