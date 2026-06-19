import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor representing batched images
input_tensor = torch.randn(2, 3, 64, 64)

# Define the target size
target_size = (128, 128)

# Apply bilinear interpolation
output_tensor = interpolate(input_tensor, size=target_size, mode='bilinear', align_corners=False)

print(output_tensor.shape)