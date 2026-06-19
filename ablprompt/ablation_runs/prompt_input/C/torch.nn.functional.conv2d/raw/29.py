import torch

# Create random input tensor of shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 64, 64)

# Create random weight tensor of shape (out_channels, in_channels // groups, kernel_height, kernel_width)
weight_tensor = torch.randn(9, 3, 3, 3)

# Create bias tensor of shape (out_channels,)
bias_tensor = torch.randn(9)

# Apply 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)  # Should be (1, 9, 64, 64)