import torch
from torch.nn import ConvTranspose2d

# Define model parameters
in_channels = 3
out_channels = 64
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
output_padding = (0, 0)
groups = 1
bias = True
dilation = (1, 1)

# Create ConvTranspose2d layer
conv_transpose2d = ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation)

# Create random input tensor
input_tensor = torch.randn(1, in_channels, 32, 32)

# Perform forward pass
output_tensor = conv_transpose2d(input_tensor)

print(output_tensor.shape)