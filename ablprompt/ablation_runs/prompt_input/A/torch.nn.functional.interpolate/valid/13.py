import torch
from torch.nn.functional import interpolate

# Create a random tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Interpolate the tensor to a new size
output_tensor = interpolate(input_tensor, scale_factor=0.5, mode='bilinear', align_corners=False)

print(output_tensor.shape)