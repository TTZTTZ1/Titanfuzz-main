import torch
import torch.nn.functional as F

# Define grid size and batch size
batch_size = 1
height, width = 32, 32

# Create random affine matrices (rotation, translation)
theta = torch.tensor([[[0.5, 0.0, 16], [0.0, 0.5, 16]]])  # Batch x 2 x 3

# Generate grid
grid = F.affine_grid(theta, (batch_size, 1, height, width))

print(grid)