import torch
import torch.nn.functional as F

# Create some input tensors
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
grid = torch.randn(1, 2, 4, 4)  # Grid tensor with batch size of 1, 2D grid, 4x4 spatial dimensions

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)