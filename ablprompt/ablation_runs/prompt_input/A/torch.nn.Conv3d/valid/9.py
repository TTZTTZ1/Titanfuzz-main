import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 5, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5, 5)

# Define a 3D convolutional layer with 6 output channels, kernel size of 3x3x3
conv_layer = nn.Conv3d(in_channels=3, out_channels=6, kernel_size=3)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 6, 3, 3, 3)