import torch
from torch.nn.functional import grid_sample

# Create a random input tensor of shape (1, 1, 64, 64)
input_tensor = torch.randn(1, 1, 64, 64)

# Create a grid tensor of shape (1, 64, 64, 2) with values in [-1, 1]
grid_tensor = torch.rand(1, 64, 64, 2) * 2 - 1

# Apply grid_sample
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 1, 64, 64])