import torch
from torch.nn.functional import conv2d

# Create a random input tensor of shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random filter tensor of shape (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(64, 3, 3, 3)

# Apply 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)