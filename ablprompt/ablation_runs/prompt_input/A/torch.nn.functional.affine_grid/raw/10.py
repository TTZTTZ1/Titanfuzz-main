import torch
import torch.nn.functional as F

# Define the size of the grid and the number of points in each dimension
size = (1, 3, 256, 256)
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])

# Generate the affine grid
grid = F.affine_grid(theta, size)

print(grid)