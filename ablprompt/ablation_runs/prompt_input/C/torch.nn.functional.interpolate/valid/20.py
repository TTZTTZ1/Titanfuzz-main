import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor with shape (1, 3, 256, 256)
input_tensor = torch.randn(1, 3, 256, 256)

# Define the desired output size
output_size = (128, 128)

# Interpolate the tensor using bilinear mode
interpolated_tensor = interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=False)

print(interpolated_tensor.shape)  # Output should be torch.Size([1, 3, 128, 128])