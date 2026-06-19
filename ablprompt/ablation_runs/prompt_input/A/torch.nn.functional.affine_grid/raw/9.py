import torch
import torch.nn.functional as F

# Define parameters for affine grid
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transformation matrix
size = (3, 256, 256)  # Output size (channels, height, width)

# Generate affine grid
grid = F.affine_grid(theta, size)

print(grid)