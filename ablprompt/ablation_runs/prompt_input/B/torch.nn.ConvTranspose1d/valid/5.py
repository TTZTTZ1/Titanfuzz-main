import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define a ConvTranspose1d layer
transpose_conv = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=5, stride=2, padding=1, output_padding=1, groups=1, bias=True, dilation=1, padding_mode='zeros')

# Apply the transposed convolution
output_tensor = transpose_conv(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 8, 64]