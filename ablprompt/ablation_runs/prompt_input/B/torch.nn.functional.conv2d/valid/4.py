import torch
import torch.nn.functional as F

# Create a random input tensor of shape (batch_size, channels_in, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random weight tensor of shape (out_channels, channels_out//groups, kernel_height, kernel_width)
weight_tensor = torch.randn(64, 3, 3, 3)

# Define other parameters
bias_tensor = torch.randn(64)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)
groups = 1

# Apply 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=stride, padding=padding, dilation=dilation, groups=groups)

print(output_tensor.shape)