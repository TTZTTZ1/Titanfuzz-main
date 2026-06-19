import torch
from torch.nn import ConvTranspose3d

# Define parameters
in_channels = 8
out_channels = 16
kernel_size = (3, 3, 3)
stride = (2, 2, 2)
padding = (1, 1, 1)
output_padding = (0, 0, 0)
groups = 1
bias = True
dilation = (1, 1, 1)

# Create ConvTranspose3d layer
conv_transpose3d = ConvTranspose3d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation)

# Example input tensor
input_tensor = torch.randn(1, in_channels, 10, 10, 10)

# Perform forward pass
output_tensor = conv_transpose3d(input_tensor)

print(output_tensor.shape)