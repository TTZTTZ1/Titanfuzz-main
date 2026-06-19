import torch
from torch.nn.functional import interpolate

# Create a random 4D tensor with shape (batch_size, channels, height, width)
input_tensor = torch.randn(2, 3, 100, 100)

# Define the target size as a tuple
target_size = (200, 200)

# Interpolate the input tensor to the target size using bilinear interpolation
output_tensor = interpolate(input_tensor, size=target_size, mode='bilinear', align_corners=False)

print(output_tensor.shape)  # Should print: torch.Size([2, 3, 200, 200])