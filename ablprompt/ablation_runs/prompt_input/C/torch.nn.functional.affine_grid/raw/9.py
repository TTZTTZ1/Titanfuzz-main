import torch
from torch.nn.functional import affine_grid

# Define the number of transformations and the output size
num_transforms = 2
output_size_2d = (10, 10)
output_size_3d = (10, 10, 10)

# Create random affine transformation matrices
theta_2d = torch.randn(num_transforms, 2, 3).float()
theta_3d = torch.randn(num_transforms, 3, 4).float()

# Generate affine grids
grid_2d = affine_grid(theta_2d, output_size_2d, align_corners=True)
grid_3d = affine_grid(theta_3d, output_size_3d, align_corners=True)

print("2D Affine Grid:", grid_2d)
print("3D Affine Grid:", grid_3d)