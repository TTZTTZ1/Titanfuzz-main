import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5)

# Define a ConvTranspose1d layer
conv_transpose_layer = nn.ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=3, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor)