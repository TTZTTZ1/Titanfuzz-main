import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 10, 10)

# Define the target size
target_size = (20, 20)

# Interpolate the tensor to the target size using bilinear interpolation
output_tensor = interpolate(input_tensor, size=target_size, mode='bilinear', align_corners=False)

print(output_tensor.shape)