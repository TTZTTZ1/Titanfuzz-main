import torch

# Define the number of transformations and the target size
batch_size = 2
height, width = 8, 8

# Create random affine transformation matrices for each batch element
theta = torch.rand(batch_size, 2, 3)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, (batch_size, 1, height, width), align_corners=True)

print(grid)