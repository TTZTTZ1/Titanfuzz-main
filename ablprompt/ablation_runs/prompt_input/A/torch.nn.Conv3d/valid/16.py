import torch
import torch.nn as nn

# Define a simple 3D convolutional layer
conv3d_layer = nn.Conv3d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)

# Create a random input tensor for the convolutional layer
input_tensor = torch.randn(1, 1, 32, 32, 32)

# Perform the forward pass through the convolutional layer
output_tensor = conv3d_layer(input_tensor)

print(output_tensor.shape)