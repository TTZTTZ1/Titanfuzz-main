import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define the ConvTranspose1d layer
conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Apply the ConvTranspose1d layer
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 8, 64])