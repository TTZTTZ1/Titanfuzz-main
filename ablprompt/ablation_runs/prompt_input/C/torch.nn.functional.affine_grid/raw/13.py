import torch

# Define the number of transformations and the size of the output grid
batch_size = 2
height = 8
width = 8

# Create random affine transformation matrices for each element in the batch
theta = torch.randn(batch_size, 2, 3)

# Define the output size of the grid
output_size = (height, width)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, output_size, align_corners=True)

print(grid)