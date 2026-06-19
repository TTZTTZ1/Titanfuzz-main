import torch
from torch.nn.functional import conv2d

# Create a random input tensor of shape (batch_size, in_channels, height, width)
batch_size = 2
in_channels = 3
height = 64
width = 64
input_tensor = torch.randn(batch_size, in_channels, height, width)

# Create a random weight tensor of shape (out_channels, in_channels // groups, kernel_height, kernel_width)
out_channels = 16
kernel_height = 5
kernel_width = 5
groups = 1
weight_tensor = torch.randn(out_channels, in_channels // groups, kernel_height, kernel_width)

# Perform 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding='same', dilation=1, groups=groups)

print(output_tensor.shape)