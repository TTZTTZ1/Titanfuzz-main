import torch
import torch.nn as nn

# Define a simple 3D convolutional transpose layer
conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=(2, 2, 2), stride=(1, 1, 1))

# Create a random input tensor of shape (batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 1, 4, 4, 4)

# Perform the forward pass through the convolutional transpose layer
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)  # Output should be (1, 1, 7, 7, 7)