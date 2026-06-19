import torch
from torch.nn.functional import interpolate

# Create a random input tensor with shape (1, 3, 10, 10)
input_tensor = torch.randn(1, 3, 10, 10)

# Interpolate the tensor to a new size of (1, 3, 20, 20) using bilinear interpolation
output_tensor = interpolate(input_tensor, size=(20, 20), mode='bilinear', align_corners=False)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 20, 20])