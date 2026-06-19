import torch
from torch.nn.functional import affine_grid

# Define the batch size and dimensions
batch_size = 2
height, width = 8, 8

# Create random affine transformation matrices for each sample in the batch
theta = torch.randn(batch_size, 2, 3)

# Define the target output size
size = (batch_size, height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)