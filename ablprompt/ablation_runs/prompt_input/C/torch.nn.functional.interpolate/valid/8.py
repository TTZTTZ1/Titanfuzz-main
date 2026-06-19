import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Interpolate the tensor to a new size using bilinear interpolation
output_tensor = interpolate(input_tensor, size=(128, 128), mode='bilinear', align_corners=False)

print(output_tensor.shape)