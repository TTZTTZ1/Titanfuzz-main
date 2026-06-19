import torch
from torch.nn.functional import interpolate

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the target size
target_size = (128, 128)

# Interpolate the input tensor to the target size using bilinear interpolation
output_tensor = interpolate(input_tensor, size=target_size, mode='bilinear', align_corners=True)

print(output_tensor.shape)