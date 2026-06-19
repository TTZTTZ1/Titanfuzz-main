import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the new size
new_size = (64, 64)

# Interpolate the tensor
output_tensor = interpolate(input_tensor, size=new_size, mode='bilinear', align_corners=False)

print(output_tensor.shape)