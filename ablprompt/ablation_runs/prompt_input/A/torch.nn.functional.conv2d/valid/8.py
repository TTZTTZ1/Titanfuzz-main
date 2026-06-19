import torch
import torch.nn.functional as F

# Create a random input tensor and a kernel
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size of 1, 3 channels, 5x5 spatial dimensions
kernel = torch.randn(3, 3, 3, 3)       # 3 output channels, 3x3 kernel, 3 input channels

# Perform convolution
output_tensor = F.conv2d(input_tensor, kernel)

print(output_tensor)