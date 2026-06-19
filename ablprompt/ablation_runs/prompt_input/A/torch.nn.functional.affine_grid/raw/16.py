import torch
import torch.nn.functional as F

# Define the size of the grid and the affine transformation parameters
batch_size = 1
num_points = 4
size = (3, 3)
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity matrix for simplicity

# Generate the grid using affine_grid
grid = F.affine_grid(theta, size, align_corners=False)

print(grid)