import torch
import torch.nn.functional as F

# Create a random input tensor (batch size=1, channels=1, height=32, width=32)
input_tensor = torch.randn(1, 1, 32, 32)

# Create a random grid tensor (batch size=1, height=16, width=16, 2)
grid_tensor = torch.randn(1, 16, 16, 2)

# Normalize the grid tensor to be within [-1, 1]
grid_tensor = (grid_tensor / 16) * 2 - 1

# Apply grid_sample
output_tensor = F.grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)  # Should print: torch.Size([1, 1, 16, 16])