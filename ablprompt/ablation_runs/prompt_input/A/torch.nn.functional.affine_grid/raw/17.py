import torch
import torch.nn.functional as F

# Define parameters for affine grid generation
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Batch size of 1, 2D transformation matrix
size = (3, 4)  # Output spatial size (channels, height, width)

# Generate the affine grid
grid = F.affine_grid(theta, size)
print(grid)