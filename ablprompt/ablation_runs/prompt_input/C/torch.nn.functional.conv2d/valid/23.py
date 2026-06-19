import torch
from torch.nn.functional import conv2d

# Create random input tensor (batch_size, channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create random weight tensor (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(6, 3, 3, 3)

# Create bias tensor (out_channels,)
bias_tensor = torch.randn(6)

# Apply convolution
output_tensor = conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)