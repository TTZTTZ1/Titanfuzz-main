import torch
import torch.nn as nn

# Define a simple convolutional layer using torch.nn.Conv2d
conv_layer = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=0)

# Create a random input tensor of shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 1, 5, 5)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 3, 3])