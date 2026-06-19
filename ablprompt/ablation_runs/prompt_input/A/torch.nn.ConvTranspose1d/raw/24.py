import torch
from torch.nn import ConvTranspose1d

# Define input tensor and parameters for ConvTranspose1d
input_tensor = torch.randn(1, 3, 5)  # Batch size 1, 3 input channels, sequence length 5
kernel_size = 4
stride = 2
padding = 1
output_padding = 0

# Create an instance of ConvTranspose1d
conv_transpose = ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding, output_padding=output_padding)

# Perform the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor)