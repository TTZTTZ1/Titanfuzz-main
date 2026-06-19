import torch

# Define the number of transformations and the target size
num_transformations = 2
target_size_2d = (1, 32, 32)
target_size_3d = (1, 32, 32, 32)

# Generate random affine transformation matrices
theta_2d = torch.randn(num_transformations, 2, 3).float()
theta_3d = torch.randn(num_transformations, 3, 4).float()

# Create the sampling grids
grid_2d = torch.nn.functional.affine_grid(theta_2d, target_size_2d, align_corners=True)
grid_3d = torch.nn.functional.affine_grid(theta_3d, target_size_3d, align_corners=True)

print("2D Grid Shape:", grid_2d.shape)
print("3D Grid Shape:", grid_3d.shape)