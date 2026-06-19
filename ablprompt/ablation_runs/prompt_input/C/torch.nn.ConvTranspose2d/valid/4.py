import torch
from torch import nn

# Define the ConvTranspose2d layer
conv_transpose = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Perform the forward pass
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)