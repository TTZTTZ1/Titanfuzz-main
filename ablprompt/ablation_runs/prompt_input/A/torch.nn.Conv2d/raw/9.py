import torch
import torch.nn as nn

# Create a simple input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define a Conv2d layer
conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)