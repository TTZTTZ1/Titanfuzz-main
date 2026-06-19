import torch
from torch.nn.functional import affine_grid

# Define the transformation matrices for a batch of 2D transformations
theta = torch.tensor([
    [[1.0, 0.0, 10.0], [0.0, 1.0, 20.0]],
    [[0.5, 0.0, 30.0], [0.0, 0.5, 40.0]]
], dtype=torch.float32)

# Define the target output size
size = (2, 3, 100, 100)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)
print(grid.shape)