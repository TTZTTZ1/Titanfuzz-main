import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
grid_tensor = torch.randn(1, 2, 4, 4)   # Batch size of 1, 2 coordinates per pixel, 4x4 spatial dimensions

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid_tensor)

print(output_tensor)