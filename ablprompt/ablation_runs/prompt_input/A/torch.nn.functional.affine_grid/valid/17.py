import torch
import torch.nn.functional as F

# Define the grid size and batch size
batch_size = 1
height, width = 32, 32

# Create an identity affine transformation matrix
theta = torch.tensor([[[1., 0., 0.], [0., 1., 0.]]])

# Generate the grid using affine_grid
grid = F.affine_grid(theta, (batch_size, 1, height, width))

print(grid)