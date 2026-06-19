import torch
import torch.nn.functional as F

# Define the size of the grid and the affine transformation parameters
batch_size = 1
num_points = 3
size = (2, 2)
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transformation

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=False)

print(grid)