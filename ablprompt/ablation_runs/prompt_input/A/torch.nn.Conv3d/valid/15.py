import torch
from torch import nn

# Define a simple 3D convolutional layer
conv_layer = nn.Conv3d(in_channels=1, out_channels=64, kernel_size=3, stride=1, padding=1)

# Create a random input tensor with shape (batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 1, 32, 32, 32)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be [1, 64, 32, 32, 32]