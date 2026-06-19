import torch
import torch.nn.functional as F

# Define a batch of 2D affine transformations
theta = torch.tensor([[[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]]], dtype=torch.float32)

# Define the size of the output grid
size = (1, 1, 4, 4)  # Batch size, channels, height, width

# Generate the affine grid
grid = F.affine_grid(theta, size)

print(grid)