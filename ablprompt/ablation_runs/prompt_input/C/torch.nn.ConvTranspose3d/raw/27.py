import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Define the ConvTranspose3d layer
conv_transpose_3d = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)

# Apply the transposed convolution
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)