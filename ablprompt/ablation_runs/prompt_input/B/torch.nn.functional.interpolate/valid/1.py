import torch
from torch.nn.functional import interpolate

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the desired output size
output_size = (128, 128)

# Interpolate the input tensor
interpolated_tensor = interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)