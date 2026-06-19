import torch
from torch import nn

# Define a simple convolutional layer
conv_layer = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=0)

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)  # Batch size of 1, 1 channel, 5x5 image

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor)