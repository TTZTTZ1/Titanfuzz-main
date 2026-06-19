import torch
import torch.nn.functional as F

# Define the number of transformations and the output size
num_transformations = 2
output_size_2d = (1, 10, 10)
output_size_3d = (1, 10, 10, 10)

# Create random affine transformation matrices
theta_2d = torch.randn(num_transformations, 2, 3)
theta_3d = torch.randn(num_transformations, 3, 4)

# Generate affine grids
grid_2d = F.affine_grid(theta_2d, output_size_2d)
grid_3d = F.affine_grid(theta_3d, output_size_3d)

print("2D Affine Grid:", grid_2d)
print("3D Affine Grid:", grid_3d)