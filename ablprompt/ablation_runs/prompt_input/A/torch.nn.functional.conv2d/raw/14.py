import torch
import torch.nn.functional as F

# Create a random input tensor (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 5, 5)

# Define a convolutional kernel
kernel = torch.randn(16, 3, 3, 3)

# Perform 2D convolution
output_tensor = F.conv2d(input_tensor, kernel, stride=1, padding=1)

print(output_tensor.shape)  # Should print: torch.Size([1, 16, 7, 7])