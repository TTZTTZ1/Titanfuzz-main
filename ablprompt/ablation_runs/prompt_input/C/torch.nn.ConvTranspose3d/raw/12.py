import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Define the ConvTranspose3d layer
conv_transpose_3d = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, output_padding=1, groups=1, bias=True, dilation=1, padding_mode='zeros')

# Apply the layer to the input tensor
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)  # Should print the shape after upsampling