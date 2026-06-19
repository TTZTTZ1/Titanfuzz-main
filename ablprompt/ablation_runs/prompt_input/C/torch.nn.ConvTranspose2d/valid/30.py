import torch
from torch.nn import ConvTranspose2d

# Define the ConvTranspose2d layer
in_channels = 16
out_channels = 33
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
output_padding = (0, 0)
groups = 1
bias = True
dilation = (1, 1)

conv_transpose = ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, output_padding, groups, bias, dilation)

# Create a random input tensor
input_tensor = torch.randn(20, in_channels, 50, 100)

# Perform the forward pass
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)