import torch
from torch.nn.functional import affine_grid

# Define the batch size, height, width for the grid
batch_size = 2
height = 32
width = 32

# Create random affine transformation matrices
theta = torch.randn(batch_size, 2, 3).to(torch.float32)

# Define the output size
size = (batch_size, 3, height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)
print(grid.shape)  # Expected shape: torch.Size([2, 3, 32, 32])