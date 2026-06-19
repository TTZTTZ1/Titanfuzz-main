import torch
from torch.nn.functional import affine_grid

# Define a batch of 2D affine transformations
theta = torch.tensor([[[1., 0., 0.], [0., 1., 0.]]])  # Batch size x 2 x 3

# Define the grid size
size = (1, 1, 4, 4)  # Batch size x Channels x Height x Width

# Generate the grid
grid = affine_grid(theta, size)

print(grid)