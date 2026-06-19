import torch
from torch.nn.functional import grid_sample

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Create a grid tensor with normalized coordinates
grid_tensor = torch.rand(1, 64, 64, 2) * 2 - 1

# Apply grid sampling
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)