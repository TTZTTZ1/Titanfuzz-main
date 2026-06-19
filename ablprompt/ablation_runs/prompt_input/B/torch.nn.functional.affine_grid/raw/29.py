import torch
from torch.nn.functional import affine_grid

# Create a batch of affine transformation matrices
batch_size = 2
theta = torch.tensor([
    [[1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0]],
    [[1.0, 0.0, 10.0],
     [0.0, 1.0, 20.0]]
], dtype=torch.float32)

# Define the target output size
size = (1, 1, 32, 32)

# Generate the affine grid
grid = affine_grid(theta, size, align_corners=True)

print(grid)