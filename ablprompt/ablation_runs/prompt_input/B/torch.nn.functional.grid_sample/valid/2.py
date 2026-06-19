import torch
from torch.nn.functional import grid_sample

# Create a random input tensor (batch size=1, channels=1, height=32, width=32)
input_tensor = torch.randn(1, 1, 32, 32)

# Create a random grid tensor (batch size=1, height=16, width=16, 2)
grid_tensor = torch.randn(1, 16, 16, 2) * 2 - 1  # Normalize to [-1, 1]

# Apply grid sample with bilinear interpolation and zero padding
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Should print: torch.Size([1, 1, 16, 16])