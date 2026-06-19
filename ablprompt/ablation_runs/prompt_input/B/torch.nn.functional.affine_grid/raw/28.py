import torch
import torch.nn.functional as F

# Create a batch of 2D affine transformation matrices
batch_size = 2
theta = torch.tensor([
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],  # Identity transform
    [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0]]   # Scaling by 0.5
], dtype=torch.float32)

# Define the target output size
size = (batch_size, 3, 4)  # Batch size, height, width

# Generate the affine grid
grid = F.affine_grid(theta, size, align_corners=True)

print(grid)