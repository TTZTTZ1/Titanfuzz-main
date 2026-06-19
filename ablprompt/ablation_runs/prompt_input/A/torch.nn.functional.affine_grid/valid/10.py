import torch
import torch.nn.functional as F

# Define grid size and batch size
batch_size = 1
height, width = 32, 32

# Create random affine parameters: (N, 2, 3)
theta = torch.randn(batch_size, 2, 3)

# Generate affine grid
grid = F.affine_grid(theta, (batch_size, 1, height, width))

print(grid.shape)  # Should print torch.Size([1, 32, 32, 2])