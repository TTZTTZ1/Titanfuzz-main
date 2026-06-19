import torch
import torch.nn.functional as F

# Define a batch of 2D affine matrices
batch_size = 1
num_points = 3
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transformation

# Generate the grid
grid = F.affine_grid(theta, (batch_size, 1, num_points, num_points))

print(grid)