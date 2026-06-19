import torch
from torch import nn

# Create a dummy input tensor of shape (1, 16, 32, 32, 32)
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define the ConvTranspose3d layer
conv_transpose_3d_layer = nn.ConvTranspose3d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_3d_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 8, 64, 64, 64)