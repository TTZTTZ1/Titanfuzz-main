import torch
from torch.nn.functional import affine_grid

# Define the batch size, number of channels, height, and width
batch_size = 2
num_channels = 3
height = 4
width = 5

# Create a random batch of affine transformation matrices
theta = torch.randn(batch_size, 2, 3)

# Define the target output size
size = (height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)