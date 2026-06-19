import torch
from torch.nn.functional import affine_grid

# Define the number of transformations and dimensions
num_transforms = 2
dim = 2  # For 2D grid

# Create random affine transformation matrices
theta = torch.randn(num_transforms, dim + 1, dim + 1)

# Define the target output size
size = (num_transforms, *([100, 100])) if dim == 2 else (num_transforms, *([100, 100, 100]))

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)