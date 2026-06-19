import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor with shape (batch_size, channels, height, width)
batch_size = 2
channels = 3
height = 32
width = 32
input_tensor = torch.randn(batch_size, channels, height, width)

# Define the desired output size
output_height = 64
output_width = 64

# Interpolate the tensor to the new size using bilinear interpolation
interpolated_tensor = interpolate(input_tensor, size=(output_height, output_width), mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)  # Should print: torch.Size([2, 3, 64, 64])