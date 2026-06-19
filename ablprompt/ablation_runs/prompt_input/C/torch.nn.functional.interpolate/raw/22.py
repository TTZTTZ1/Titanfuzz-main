import torch
from torch.nn.functional import interpolate

# Create a random input tensor of shape (1, 3, 32, 32)
input_tensor = torch.randn(1, 3, 32, 32)

# Interpolate the tensor to a new size of (1, 3, 64, 64) using bilinear interpolation
output_tensor = interpolate(input_tensor, size=(64, 64), mode='bilinear', align_corners=True)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 64, 64])