import torch
import torch.nn.functional as F

# Define the number of transformations and dimensions
batch_size = 2
height = 4
width = 4

# Create random affine transformation matrices for each element in the batch
theta = torch.randn(batch_size, 2, 3).to(torch.float32)

# Define the target output size
size = (batch_size, height, width)

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=True)

print(grid)