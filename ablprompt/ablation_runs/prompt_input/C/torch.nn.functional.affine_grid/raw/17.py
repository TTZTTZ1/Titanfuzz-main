import torch

# Define the number of transformations and dimensions
num_transformations = 2
height, width = 8, 8

# Create random affine transformation matrices for 2D
theta = torch.randn(num_transformations, 2, 3)

# Define the target output size
size = (num_transformations, height, width)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, size, align_corners=True)

print(grid)