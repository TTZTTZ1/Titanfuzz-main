import torch
import torch.nn as nn

# Define the ConvTranspose2d layer
conv_transpose = nn.ConvTranspose2d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, output_padding=1)

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50, 100)

# Perform the forward pass
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)