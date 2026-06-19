import torch
import torch.nn.functional as F

# Define a batch of transformation matrices (batch_size, 2D/3D, 4)
theta = torch.tensor([[[1., 0., 0.], [0., 1., 0.]]])  # For 2D grid
grid = F.affine_grid(theta, size=torch.Size((1, 1, 64, 64)))

print(grid.shape)  # Should print: torch.Size([1, 2, 64, 64])