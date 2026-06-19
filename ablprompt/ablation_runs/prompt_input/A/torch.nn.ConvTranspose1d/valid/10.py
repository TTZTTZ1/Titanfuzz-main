import torch
from torch import nn

# Define the input tensor and parameters for ConvTranspose1d
input_tensor = torch.randn(1, 3, 5)  # Batch size=1, in_channels=3, sequence_length=5
kernel_size = 2
stride = 1
padding = 0
output_padding = 0
groups = 1
bias = True
dilation = 1

# Create an instance of ConvTranspose1d
conv_transpose1d = nn.ConvTranspose1d(in_channels=input_tensor.size(1), out_channels=64, kernel_size=kernel_size, stride=stride, padding=padding, output_padding=output_padding, groups=groups, bias=bias, dilation=dilation)

# Perform the forward pass
output_tensor = conv_transpose1d(input_tensor)

print(output_tensor.shape)