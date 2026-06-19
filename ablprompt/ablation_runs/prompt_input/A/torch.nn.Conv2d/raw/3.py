import torch
import torch.nn as nn

# Create a convolutional layer
conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)

# Example input tensor (batch size 1, channels 3, height 32, width 32)
input_tensor = torch.randn(1, 3, 32, 32)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 64, 32, 32]