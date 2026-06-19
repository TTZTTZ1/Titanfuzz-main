import torch
from torch.nn.functional import conv2d

# Create a random input tensor with shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random weight tensor with shape (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(64, 3, 3, 3)

# Create a bias tensor with shape (out_channels,)
bias_tensor = torch.randn(64)

# Apply 2D convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=2, padding=1, dilation=1, groups=1)

print(output_tensor.shape)