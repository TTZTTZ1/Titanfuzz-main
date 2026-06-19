import torch
import torch.nn.functional as F

# Define the size of the grid and the number of transformations
grid_size = (1, 2, 3, 4)  # batch_size, channels, height, width
num_transforms = 5

# Create random affine parameters
theta = torch.randn(num_transforms, 2, 3)

# Generate the grid
grid = F.affine_grid(theta, grid_size)

print(grid)