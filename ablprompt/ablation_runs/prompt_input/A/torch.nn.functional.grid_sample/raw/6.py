import torch
import torch.nn.functional as F

# Create an input tensor and a grid
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
grid = torch.randn(1, 4, 4, 2)  # Batch size of 1, 4x4 grid points, each point has (x, y) coordinates

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)