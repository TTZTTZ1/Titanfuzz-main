import torch
from torch.nn.functional import grid_sample

# Create a random input tensor of shape (1, 1, 16, 16)
input_tensor = torch.randn(1, 1, 16, 16)

# Create a random grid tensor of shape (1, 8, 8, 2)
grid_tensor = torch.randn(1, 8, 8, 2)

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Should print torch.Size([1, 1, 8, 8])