import torch
import torch.nn.functional as F

# Define grid size and batch size
batch_size = 1
height, width = 32, 32

# Create random affine parameters (rotation, translation)
theta = torch.tensor([[[0.5, 0.0, 16], [0.0, 0.5, 16]]])  # Rotation by 45 degrees and translation by 16 pixels in both directions

# Generate the grid
grid = F.affine_grid(theta, torch.Size((batch_size, 1, height, width)))

print(grid)