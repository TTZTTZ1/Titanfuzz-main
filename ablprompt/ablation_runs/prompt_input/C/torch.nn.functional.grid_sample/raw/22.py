import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 1, 32, 32)

# Create a grid of normalized coordinates
grid = torch.rand(1, 64, 64, 2) * 2 - 1  # Normalize to [-1, 1]

# Apply grid_sample
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)