import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Interpolate the tensor to a new size using bilinear mode
output_tensor = interpolate(input_tensor, size=(64, 64), mode='bilinear', align_corners=False)

print(output_tensor.shape)