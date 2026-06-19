import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 3, 256, 256)  # Batch size of 1, 3 channels, 256x256 image
grid_tensor = torch.randn(1, 256, 256, 2)   # Grid of shape (batch_size, height, width, 2)

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)