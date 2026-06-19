import torch
import torch.nn as nn

# Define a simple input tensor
input_tensor = torch.randn(1, 3, 32, 32)  # Batch size of 1, 3 channels, 32x32 image

# Create a Conv2d layer with 6 output channels, kernel size of 5
conv_layer = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=5)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 6, 28, 28]