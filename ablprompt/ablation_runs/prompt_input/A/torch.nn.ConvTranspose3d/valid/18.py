import torch
from torch import nn

# Define input tensor and parameters for ConvTranspose3d
input_tensor = torch.randn(1, 3, 64, 64, 64)
kernel_size = (3, 3, 3)
stride = (2, 2, 2)
padding = (1, 1, 1)

# Create an instance of ConvTranspose3d
conv_transpose_3d = nn.ConvTranspose3d(in_channels=3, out_channels=64, kernel_size=kernel_size, stride=stride, padding=padding)

# Perform the forward pass
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 64, 128, 128, 128]