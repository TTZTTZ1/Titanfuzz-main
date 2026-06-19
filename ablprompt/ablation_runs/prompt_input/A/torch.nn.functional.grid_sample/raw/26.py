import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 1, 32, 32)
grid = torch.rand(1, 32, 32, 2) * 2 - 1  # Grid values should be in [-1, 1]

# Call grid_sample
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor.shape)