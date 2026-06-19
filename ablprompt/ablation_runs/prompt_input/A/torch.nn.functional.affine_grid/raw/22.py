import torch
import torch.nn.functional as F

# Define a batch of transformation matrices (batch_size, num_points, 2)
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]], dtype=torch.float32)

# Define the size of the grid
size = torch.Size((1, 1, 4, 4))

# Generate the affine grid
grid = F.affine_grid(theta, size)

print(grid)