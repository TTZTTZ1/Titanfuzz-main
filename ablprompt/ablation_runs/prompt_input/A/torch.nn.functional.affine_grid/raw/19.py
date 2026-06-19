import torch
import torch.nn.functional as F

# Define a batch of 2D affine matrices (batch_size, num_points, 2)
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                      [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0]]])

# Define the size of the output grid
size = (3, 3)  # height, width

# Generate the affine grid
grid = F.affine_grid(theta, size)

print(grid)