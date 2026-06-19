import torch
from torch import nn

# Define a simple 3D convolutional layer
conv_layer = nn.Conv3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=True)

# Create a random input tensor with shape (batch_size, in_channels, D, H, W)
input_tensor = torch.randn(4, 16, 32, 32, 32)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: (4, 32, 32, 32, 32)