import torch
import torch.nn as nn

# Define a simple input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Create an instance of ConvTranspose2d
conv_transpose_layer = nn.ConvTranspose2d(in_channels=3, out_channels=6, kernel_size=5, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)