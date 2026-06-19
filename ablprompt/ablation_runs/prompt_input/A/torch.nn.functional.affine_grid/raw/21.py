import torch
import torch.nn.functional as F

# Define the grid size and batch size
grid_size = (3, 256, 256)
batch_size = 4

# Create random affine parameters
theta = torch.randn(batch_size, 2, 3)

# Generate the affine grid
grid = F.affine_grid(theta, grid_size)

print(grid.shape)  # Should print: torch.Size([4, 3, 256, 256])