import torch
import torch.nn.functional as F

# Define the grid size and batch size
grid_size = (2, 3, 4)
batch_size = 1

# Create random affine parameters (rotation, translation, scale)
theta = torch.randn(batch_size, 2, 3)

# Generate the affine grid
grid = F.affine_grid(theta, grid_size, align_corners=False)

print(grid)