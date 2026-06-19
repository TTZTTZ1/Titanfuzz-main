import torch
import torch.nn.functional as F

# Define the batch size, number of channels, and spatial dimensions
batch_size = 2
num_channels = 3
height = 4
width = 5

# Create a random transformation matrix for each image in the batch
theta = torch.rand(batch_size, 2, 3)

# Generate the grid using affine_grid
grid = F.affine_grid(theta, (batch_size, num_channels, height, width))

print(grid)