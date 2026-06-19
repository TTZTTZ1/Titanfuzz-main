import torch
from torch.nn.functional import grid_sample

# Create a random input tensor (batch_size=1, channels=1, height=64, width=64)
input_tensor = torch.randn(1, 1, 64, 64)

# Create a grid tensor with normalized coordinates (batch_size=1, height=32, width=32, 2)
grid_tensor = torch.rand(1, 32, 32, 2) * 2 - 1

# Apply grid_sample with bilinear interpolation and reflection padding
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='reflection')

print(output_tensor.shape)  # Should be torch.Size([1, 1, 32, 32])