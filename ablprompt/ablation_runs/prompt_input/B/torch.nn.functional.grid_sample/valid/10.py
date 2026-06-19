import torch
from torch.nn.functional import grid_sample

# Create a random input tensor and a corresponding grid
batch_size = 1
channels = 3
height_in = 64
width_in = 64
height_out = 32
width_out = 32

input_tensor = torch.randn(batch_size, channels, height_in, width_in)
grid = torch.rand(batch_size, height_out, width_out, 2) * 2 - 1  # Normalize grid coordinates to [-1, 1]

# Apply grid_sample
output_tensor = grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)