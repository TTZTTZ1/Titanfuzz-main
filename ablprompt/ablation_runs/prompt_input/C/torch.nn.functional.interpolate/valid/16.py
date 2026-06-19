import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor with batch size 1, channels 3, height 256, width 256
input_tensor = torch.randn(1, 3, 256, 256)

# Define the desired output size
output_size = (512, 512)

# Interpolate the tensor using bilinear method
interpolated_tensor = interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)