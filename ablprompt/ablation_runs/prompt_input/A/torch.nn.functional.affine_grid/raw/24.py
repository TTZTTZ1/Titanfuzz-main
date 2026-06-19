import torch
import torch.nn.functional as F

# Define the batch size, number of channels, height, and width
batch_size = 2
num_channels = 3
height = 4
width = 5

# Create a tensor of shape (batch_size, num_channels, height, width)
grid = torch.rand((batch_size, num_channels, height, width))

# Define the affine transformation matrix
theta = torch.tensor([[[1., 0., 0.], [0., 1., 0.]]])  # Identity transform for simplicity

# Generate the grid using affine_grid
output_grid = F.affine_grid(theta, grid.size(), align_corners=False)

print(output_grid)