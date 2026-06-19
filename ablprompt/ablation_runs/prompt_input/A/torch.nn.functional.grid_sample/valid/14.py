import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, 3 channels, 4x4 spatial dimensions
grid = torch.rand(1, 4, 4, 2) - 0.5  # Grid coordinates in range [-0.5, 0.5]

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)