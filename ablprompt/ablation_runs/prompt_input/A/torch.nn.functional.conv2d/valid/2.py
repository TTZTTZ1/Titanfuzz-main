import torch
import torch.nn.functional as F

# Create a random input tensor (batch_size, channels, height, width)
input_tensor = torch.randn(1, 3, 5, 5)

# Create a random convolutional kernel (out_channels, in_channels, kernel_height, kernel_width)
kernel = torch.randn(1, 3, 3, 3)

# Apply the conv2d function
output_tensor = F.conv2d(input_tensor, kernel)

print(output_tensor)