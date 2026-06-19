import torch
import torch.nn.functional as F

# Create an input tensor and a grid
input_tensor = torch.randn(1, 1, 3, 3)
grid = torch.tensor([[[[0.5, 0.5], [1.5, 1.5]]]])

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)