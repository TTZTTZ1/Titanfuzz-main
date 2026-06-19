import torch

# Create random input tensor with shape (batch_size, in_channels, height, width)
batch_size = 2
in_channels = 3
height = 32
width = 32
input_tensor = torch.randn(batch_size, in_channels, height, width)

# Create random weight tensor with shape (out_channels, in_channels // groups, kernel_height, kernel_width)
out_channels = 6
kernel_height = 5
kernel_width = 5
groups = 1
weight_tensor = torch.randn(out_channels, in_channels // groups, kernel_height, kernel_width)

# Apply 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding='same', dilation=1, groups=groups)

print(output_tensor.shape)