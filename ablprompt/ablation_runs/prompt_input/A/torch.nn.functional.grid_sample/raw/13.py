import torch
import torch.nn.functional as F

# Create an input tensor and a grid
input_tensor = torch.randn(1, 3, 4, 4)
grid = torch.rand(1, 3, 2, 2) * 2 - 1  # Normalized coordinates in [-1, 1]

# Call grid_sample
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)