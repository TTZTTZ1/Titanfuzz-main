import torch
import torch.nn.functional as F

# Define the batch size and dimensions
batch_size = 2
height = 32
width = 32

# Create random affine transformation matrices
theta = torch.randn(batch_size, 2, 3).to(torch.float32)

# Define the target output size
size = (batch_size, height, width)

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=True)

print(grid)