import torch
import torch.nn.functional as F

# Create a batch of 2x3 affine transformation matrices
batch_size = 2
theta = torch.tensor([
    [[1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0]],
    [[0.5, 0.0, 0.0],
     [0.0, 0.5, 0.0]]
], dtype=torch.float32)

# Define the target output size
size = (batch_size, 1, 4, 4)

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=True)

print(grid)