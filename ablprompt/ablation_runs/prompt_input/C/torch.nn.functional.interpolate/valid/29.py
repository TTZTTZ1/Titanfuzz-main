import torch
from torch.nn.functional import interpolate

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the desired output size
output_size = (64, 64)

# Interpolate the input tensor to the desired size using bilinear interpolation
interpolated_tensor = interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)