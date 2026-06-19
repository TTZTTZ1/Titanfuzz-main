import torch
import torch.nn.functional as F

# Define the batch size, number of channels, height, and width
batch_size = 2
num_channels = 3
height = 4
width = 5

# Create random affine transformation matrices for a 2D grid
theta = torch.randn(batch_size, 2, 3)

# Define the target output size
size = (height, width)

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=True)

print(grid)