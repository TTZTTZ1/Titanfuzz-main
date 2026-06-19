import torch
from torch.nn.functional import affine_grid

# Define a batch of affine transformation matrices for 2D transformations
theta = torch.tensor([
    [[1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0]],
    [[0.5, 0.0, 0.0],
     [0.0, 0.5, 0.0]]
], dtype=torch.float32)

# Define the target output size
size = (2, 3, 3)  # Batch size 2, height 3, width 3

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)