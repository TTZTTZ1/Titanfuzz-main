import torch
from torch.nn.functional import affine_grid

# Define the grid size and batch size
batch_size = 1
height, width = 32, 32

# Create a tensor of shape (batch_size, 2, height, width) for the grid
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]]) * batch_size

# Generate the affine grid
grid = affine_grid(theta, (batch_size, 1, height, width))

print(grid)