import torch
import torch.nn.functional as F

# Create a random input tensor (batch_size, channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random weight tensor (out_channels, in_channels, kernel_height, kernel_width)
weight_tensor = torch.randn(64, 3, 5, 5)

# Perform convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=2)

print(output_tensor.shape)