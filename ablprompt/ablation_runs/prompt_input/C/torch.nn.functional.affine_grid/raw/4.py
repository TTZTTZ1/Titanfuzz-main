import torch
from torch.nn.functional import affine_grid

# Define the number of transformations and the target size
batch_size = 2
height, width = 64, 64

# Create random affine transformation matrices
theta = torch.randn(batch_size, 2, 3).to(dtype=torch.float32)

# Define the target output size
size = (batch_size, height, width)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)