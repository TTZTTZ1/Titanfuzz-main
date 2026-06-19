import torch
import torch.nn.functional as F

# Define the grid size and batch size
grid_size = (1, 3, 2, 2)
batch_size = 1

# Create a random affine matrix for each image in the batch
theta = torch.rand((batch_size, 2, 3))

# Generate the grid using the affine_matrix
grid = F.affine_grid(theta, grid_size)

print(grid)