import torch

# Define the number of transformations and the target size
num_transformations = 2
target_size = (1, 3, 28, 28)

# Create random affine transformation matrices
theta = torch.randn(num_transformations, 2, 3).double()

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, target_size, align_corners=True)

print(grid)