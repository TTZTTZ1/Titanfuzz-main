import torch
import torch.nn as nn

# Define the ConvTranspose2d layer
conv_transpose = nn.ConvTranspose2d(in_channels=32, out_channels=64, kernel_size=3, stride=2, padding=1, bias=True)

# Create a random input tensor
input_tensor = torch.randn(1, 32, 32, 32)

# Perform the forward pass
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)