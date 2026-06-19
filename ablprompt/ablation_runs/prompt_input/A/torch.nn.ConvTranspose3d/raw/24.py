import torch
from torch.nn import ConvTranspose3d

# Define input tensor
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Initialize ConvTranspose3d layer
conv_transpose_layer = ConvTranspose3d(in_channels=3, out_channels=6, kernel_size=3, stride=2, padding=1)

# Perform convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)