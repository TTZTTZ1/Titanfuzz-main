import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 1, 32, 32)

# Create a corresponding grid tensor
grid = torch.rand(1, 32, 32, 2) * 2 - 1  # Normalize coordinates to [-1, 1]

# Apply grid_sample
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)