import torch
import torch.nn as nn

# Define a simple 3D convolutional transpose layer
conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Apply the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)