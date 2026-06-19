import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 10, 10)

# Define the target size and mode
target_size = (20, 20)
interpolation_mode = 'bilinear'

# Apply interpolation
output_tensor = interpolate(input_tensor, size=target_size, mode=interpolation_mode, align_corners=True)

print(output_tensor.shape)