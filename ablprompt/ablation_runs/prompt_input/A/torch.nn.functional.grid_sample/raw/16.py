import torch
import torch.nn.functional as F

# Create an input tensor and a grid
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
grid = torch.randn(1, 3, 2, 2)  # Batch size of 1, 3 points, 2D coordinates

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)