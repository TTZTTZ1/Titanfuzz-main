import torch

# Create a batch of affine transformation matrices for a 2D grid
batch_size = 2
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                      [[1.0, 0.0, 10.0], [0.0, 1.0, 20.0]]], dtype=torch.float32)

# Define the target output size
size = (batch_size, 1, 32, 32)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, size, align_corners=True)

print(grid)