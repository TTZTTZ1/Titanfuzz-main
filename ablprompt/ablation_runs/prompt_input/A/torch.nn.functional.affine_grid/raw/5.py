import torch
import torch.nn.functional as F

# Define the grid size and batch size
batch_size = 1
height, width = 32, 32

# Create an identity affine matrix
identity_matrix = torch.tensor([[[[1., 0., 0.], [0., 1., 0.]]]])

# Repeat the identity matrix for the batch size
grid = F.affine_grid(identity_matrix.repeat(batch_size, 1), (batch_size, 1, height, width))

print(grid)