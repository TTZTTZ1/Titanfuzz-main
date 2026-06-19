import torch
from torch import nn

# Define the ConvTranspose3d layer
conv_transpose3d = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(20, 16, 10, 50, 100)

# Perform the forward pass through the ConvTranspose3d layer
output_tensor = conv_transpose3d(input_tensor)

# Print the shapes of the input and output tensors
print("Input tensor shape:", input_tensor.shape)
print("Output tensor shape:", output_tensor.shape)