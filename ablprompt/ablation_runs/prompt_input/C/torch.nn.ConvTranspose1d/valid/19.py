import torch
from torch.nn import ConvTranspose1d

# Define the parameters for the ConvTranspose1d layer
in_channels = 16
out_channels = 8
kernel_size = 3
stride = 2
padding = 1
output_padding = 0
groups = 1
bias = True
dilation = 1
padding_mode = 'zeros'

# Create an instance of ConvTranspose1d
conv_transpose = ConvTranspose1d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation, padding_mode)

# Generate a random input tensor
input_tensor = torch.randn(1, in_channels, 10)

# Perform the forward pass through the ConvTranspose1d layer
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)