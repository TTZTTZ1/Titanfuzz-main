import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 3, 4, 4)
grid_tensor = torch.rand(1, 3, 4, 2) * 2 - 1

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid_tensor)

print(output_tensor)