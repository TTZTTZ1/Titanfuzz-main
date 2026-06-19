import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the ConvTranspose2d layer
conv_transpose_layer = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=3, stride=2, padding=1, bias=True)

# Apply the layer to the input tensor
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 64, 64, 64])