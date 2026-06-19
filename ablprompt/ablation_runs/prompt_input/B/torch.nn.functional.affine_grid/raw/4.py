import torch

# Create a batch of random affine transformation matrices
batch_size = 2
theta = torch.randn(batch_size, 3, 4)

# Define the target output size
size = (batch_size, 3, 256, 256)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, size, align_corners=True)

print(grid)