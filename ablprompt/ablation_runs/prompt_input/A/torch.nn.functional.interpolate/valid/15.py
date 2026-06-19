import torch
from torch.nn import functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define interpolation parameters
size = (128, 128)
mode = 'bilinear'
align_corners = False

# Call the interpolate function
output_tensor = F.interpolate(input_tensor, size=size, mode=mode, align_corners=align_corners)

print(output_tensor.shape)  # Output should be [1, 3, 128, 128]