import torch
from torch.nn.functional import affine_grid

# Define the transformation matrices (batch of 2x3 matrices for 2D)
theta = torch.tensor([[[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]],
                      [[0.5, 0.0, 50.0],
                       [0.0, 0.5, 50.0]]], dtype=torch.float32)

# Define the target output size (batch size, height, width)
size = (2, 100, 100)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)