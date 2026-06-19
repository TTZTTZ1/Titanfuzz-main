import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 1, 64, 64)
input_tensor = torch.randn(1, 1, 64, 64)

# Create a grid of shape (1, 64, 64, 2) with values in [-1, 1]
grid = torch.rand(1, 64, 64, 2) * 2 - 1

# Apply grid_sample
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)  # Should print torch.Size([1, 1, 64, 64])