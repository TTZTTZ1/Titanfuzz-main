import torch
import torch.nn.functional as F

# Define a batch of 2D affine transformations
batch_size = 1
num_points = 4
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transformation

# Generate grid points
grid = F.affine_grid(theta, (batch_size, 3, num_points, num_points))

print(grid)