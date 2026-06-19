import torch
import torch.nn.functional as F

# Create a random input tensor (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# Create a random convolutional kernel (out_channels, in_channels, kernel_height, kernel_width)
kernel = torch.randn(64, 3, 3, 3)

# Apply the conv2d function
output_tensor = F.conv2d(input_tensor, kernel, stride=1, padding=1)

print(output_tensor.shape)  # Output shape should be (batch_size, out_channels, output_height, output_width)