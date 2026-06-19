import torch
from torch.nn.functional import affine_grid

# Define the batch size and dimensions
batch_size = 2
height, width = 64, 64

# Create random affine transformation matrices
theta = torch.randn(batch_size, 2, 3).to(torch.float32)

# Define the target output size
size = (batch_size, height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)