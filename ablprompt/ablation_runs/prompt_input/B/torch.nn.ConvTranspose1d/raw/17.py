import torch
from torch.nn import ConvTranspose1d

# Define the input tensor
input_tensor = torch.randn(1, 16, 32)

# Create an instance of ConvTranspose1d
upsample = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros')

# Perform the transposed convolution
output_tensor = upsample(input_tensor)

print(output_tensor.shape)