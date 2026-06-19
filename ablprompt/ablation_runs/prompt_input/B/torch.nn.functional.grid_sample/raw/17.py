import torch
from torch.nn.functional import grid_sample

# Create a random input tensor and a corresponding grid
input_tensor = torch.randn(1, 3, 64, 64)
grid = torch.rand(1, 64, 64, 2) * 2 - 1  # Normalize grid coordinates to [-1, 1]

# Apply grid_sample
output_tensor = grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)