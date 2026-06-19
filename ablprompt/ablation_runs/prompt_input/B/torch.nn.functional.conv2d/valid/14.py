import torch
from torch.nn.functional import conv2d

# Create random input tensor with shape (batch_size, channels_in, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create random filter weights with shape (out_channels, channels_out, kernel_height, kernel_width)
weight_tensor = torch.randn(6, 3, 3, 3)

# Perform 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)