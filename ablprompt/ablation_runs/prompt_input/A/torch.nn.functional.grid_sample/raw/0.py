import torch
import torch.nn.functional as F

# Create input tensor and grid
input_tensor = torch.randn(1, 3, 4, 4)
grid = torch.rand(1, 3, 2, 2) * 2 - 1  # Grid values should be in [-1, 1]

# Call grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)