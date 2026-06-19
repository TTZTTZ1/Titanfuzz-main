import torch

# Create random input tensor of shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create random weight tensor of shape (out_channels, in_channels/groups, kernel_height, kernel_width)
weight_tensor = torch.randn(6, 3, 5, 5)

# Define bias tensor if needed
bias_tensor = torch.randn(6)

# Perform 2D convolution
output_tensor = torch.nn.functional.conv2d(input_tensor, weight_tensor, bias=bias_tensor, stride=1, padding='same', dilation=1, groups=1)

print(output_tensor.shape)  # Should print: torch.Size([1, 6, 32, 32])