import torch
import torch.nn.functional as F

# Create input tensor and grid
input_tensor = torch.randn(1, 3, 256, 256)  # Batch size of 1, 3 channels, 256x256 image
grid = torch.randn(1, 256, 256, 2)  # Grid of shape (batch_size, height, width, 2)

# Call grid_sample function
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)