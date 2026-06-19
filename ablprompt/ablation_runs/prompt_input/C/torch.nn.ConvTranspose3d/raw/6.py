import torch
from torch.nn import ConvTranspose3d

# Define the parameters for the ConvTranspose3d layer
in_channels = 16
out_channels = 33
kernel_size = (3, 3, 3)
stride = (2, 2, 2)
padding = (1, 1, 1)
output_padding = (0, 0, 0)
groups = 1
bias = True
dilation = (1, 1, 1)

# Create an instance of ConvTranspose3d
conv_transpose_3d = ConvTranspose3d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation)

# Generate a random input tensor
input_tensor = torch.randn(20, in_channels, 10, 50, 100)

# Perform the forward pass through the ConvTranspose3d layer
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)