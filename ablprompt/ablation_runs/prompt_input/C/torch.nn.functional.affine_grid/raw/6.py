import torch

# Define the number of transformations and the size of the output grid
num_transforms = 2
output_size = (1, 32, 32)

# Create random affine transformation matrices for each transform
theta = torch.randn(num_transforms, 2, 3, dtype=torch.float32)

# Generate the affine grid using the transformation matrices and output size
grid = torch.nn.functional.affine_grid(theta, output_size, align_corners=True)

print(grid)