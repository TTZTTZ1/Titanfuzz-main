import torch
from torch.nn import ConvTranspose1d

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define the ConvTranspose1d layer
transpose_conv = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=5, stride=2, padding=1, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)

# Apply the transposed convolution
output_tensor = transpose_conv(input_tensor)

print(output_tensor.shape)