import torch
import torch.nn.functional as F

# Define the number of transformations and dimensions
batch_size = 2
height, width = 32, 32

# Create random affine transformation matrices
theta = torch.randn(batch_size, 2, 3).to(torch.float32)

# Define the output size
output_size = (batch_size, height, width)

# Generate the affine grid
grid = F.affine_grid(theta, output_size, align_corners=False)

print(grid)