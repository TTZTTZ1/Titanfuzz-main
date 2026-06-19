import torch
from torch.nn.functional import affine_grid

# Define a batch of affine transformation matrices
theta = torch.tensor([[[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]],
                      [[0.5, 0.0, 10.0],
                       [0.0, 0.5, 20.0]]], dtype=torch.float32)

# Define the target output size
size = (2, 3, 100, 100)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)