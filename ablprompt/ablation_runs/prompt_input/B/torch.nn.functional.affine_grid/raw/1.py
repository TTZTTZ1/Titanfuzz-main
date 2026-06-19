import torch
from torch.nn.functional import affine_grid

# Define the batch size, number of channels, height, and width
batch_size = 2
num_channels = 3
height = 4
width = 5

# Create a random affine transformation matrix for each element in the batch
theta = torch.randn(batch_size, num_channels // 3 * 2 + 1, num_channels // 3 * 3 + 1)

# Define the target output size
size = (batch_size, num_channels, height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)