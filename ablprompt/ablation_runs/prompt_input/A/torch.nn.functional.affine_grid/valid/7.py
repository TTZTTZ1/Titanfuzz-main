import torch
import torch.nn.functional as F

# Define the size of the grid and the affine transformation matrix
grid_size = (1, 2, 3, 4)  # Batch size, channels, height, width
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Affine transformation matrix

# Generate the grid
grid = F.affine_grid(theta, grid_size)

print(grid)