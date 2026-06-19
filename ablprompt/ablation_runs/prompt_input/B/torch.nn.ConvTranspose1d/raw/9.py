import torch
from torch.nn import ConvTranspose1d

# Define the input tensor
input_tensor = torch.randn(1, 16, 32)

# Create a ConvTranspose1d layer
transpose_conv = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1, output_padding=1)

# Apply the transpose convolution
output_tensor = transpose_conv(input_tensor)

print(output_tensor.shape)