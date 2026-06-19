import torch
from torch.nn.functional import affine_grid

# Define the affine transformation matrix (batch size = 1)
theta = torch.tensor([[[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]]], dtype=torch.float32)

# Define the target output size (batch size = 1, height = 2, width = 2)
size = (1, 2, 2)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)