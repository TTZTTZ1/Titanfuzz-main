import torch
from torch.nn.functional import conv2d

# Create random input tensor of shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create random weight tensor of shape (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(6, 3, 3, 3)

# Create optional bias tensor of shape (out_channels,)
bias_tensor = torch.randn(6)

# Define convolutional parameters
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)
groups = 1

# Apply 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=stride, padding=padding, dilation=dilation, groups=groups)

print(output_tensor.shape)