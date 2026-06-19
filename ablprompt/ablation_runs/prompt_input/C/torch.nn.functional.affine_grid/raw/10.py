import torch

# Define the batch size, height, width, and depth
batch_size = 2
height = 8
width = 8
depth = 8

# Create random affine transformation matrices for 3D case
theta = torch.randn(batch_size, 3, 4)

# Define the target output size
size = (batch_size, depth, height, width)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, size, align_corners=True)

print(grid)