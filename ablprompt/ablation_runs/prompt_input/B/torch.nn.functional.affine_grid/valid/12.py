import torch

# Define a batch of affine transformation matrices
theta = torch.tensor([[[1.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0]],
                     [[0.5, 0.0, 0.0],
                      [0.0, 0.5, 0.0]]], dtype=torch.float32)

# Define the target output size
size = (2, 3, 4, 5)

# Generate the affine grid
grid = torch.nn.functional.affine_grid(theta, size, align_corners=True)

print(grid)