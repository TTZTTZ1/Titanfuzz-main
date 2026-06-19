import torch
from torch import nn

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define a ConvTranspose2d layer
conv_transpose_layer = nn.ConvTranspose2d(in_channels=3, out_channels=6, kernel_size=5, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)