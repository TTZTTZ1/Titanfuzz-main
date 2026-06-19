import torch
import torch.nn.functional as F

# Define the grid size and batch size
grid_size = (3, 2)
batch_size = 1

# Create an identity matrix for affine transformation
identity_matrix = torch.eye(4).unsqueeze(0).repeat(batch_size, 1, 1)

# Generate the affine grid
affine_grid = F.affine_grid(identity_matrix, torch.Size([batch_size] + list(grid_size) + [3]))

print(affine_grid)