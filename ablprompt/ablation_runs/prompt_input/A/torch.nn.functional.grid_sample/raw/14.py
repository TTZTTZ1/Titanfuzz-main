import torch
import torch.nn.functional as F

# Create an input tensor and a grid
input_tensor = torch.randn(1, 3, 4, 4)
grid = torch.rand(1, 2, 4, 4) * 2 - 1  # Grid values should be in the range [-1, 1]

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)