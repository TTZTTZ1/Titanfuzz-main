import torch
import torch.nn as nn

# Create a simple convolutional layer
conv_layer = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)

# Example input tensor (batch size of 1, 3 channels, 32x32 image)
input_tensor = torch.randn(1, 3, 32, 32)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 16, 32, 32])