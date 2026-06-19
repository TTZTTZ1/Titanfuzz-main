import torch
from torch.nn.functional import interpolate

# Create a random input tensor of shape (1, 3, 10, 10)
input_tensor = torch.randn(1, 3, 10, 10)

# Define the desired output size
output_size = (20, 20)

# Interpolate the input tensor to the new size using bilinear interpolation
interpolated_tensor = interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)  # Output should be torch.Size([1, 3, 20, 20])