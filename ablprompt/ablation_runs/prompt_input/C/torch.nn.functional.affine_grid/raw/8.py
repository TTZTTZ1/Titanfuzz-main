import torch
from torch.nn.functional import affine_grid

# Define the affine transformation matrix theta
theta = torch.tensor([[[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]]])

# Define the target output size
size = (1, 3, 3)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)