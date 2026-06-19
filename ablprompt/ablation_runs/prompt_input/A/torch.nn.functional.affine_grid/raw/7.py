import torch
import torch.nn.functional as F

# Define parameters for affine grid generation
theta = torch.tensor([[[1., 0., 0.], [0., 1., 0.]]])  # Batch size x 2x3 transformation matrix
size = (1, 1, 4, 4)  # Output size (batch_size, channels, height, width)

# Generate affine grid
grid = F.affine_grid(theta, size)

print(grid)