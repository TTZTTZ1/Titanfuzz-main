import torch
from torch.nn import Conv3d

# Define input tensor dimensions
batch_size = 4
in_channels = 8
out_channels = 16
depth = 32
height = 32
width = 32

# Create a random input tensor
input_tensor = torch.randn(batch_size, in_channels, depth, height, width)

# Define convolutional layer parameters
kernel_size = (3, 3, 3)
stride = (1, 1, 1)
padding = (1, 1, 1)
dilation = (1, 1, 1)
groups = 1
bias = True
padding_mode = 'zeros'

# Create the Conv3d layer
conv_layer = Conv3d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size,
                    stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias,
                    padding_mode=padding_mode)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)