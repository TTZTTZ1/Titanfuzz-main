import torch
import torch.nn.functional as F

# Define the grid size and batch size
grid_size = (1, 2, 3, 4)  # Batch size, channels, height, width
batch_size = grid_size[0]

# Create a random affine transformation matrix
theta = torch.rand(batch_size, 2, 3)

# Generate the affine grid
grid = F.affine_grid(theta, grid_size)

print(grid)