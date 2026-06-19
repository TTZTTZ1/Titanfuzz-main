import torch
import torch.nn.functional as F

# Create random input tensor with shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create random weight tensor with shape (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(6, 3, 3, 3)

# Perform 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, bias=None, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)