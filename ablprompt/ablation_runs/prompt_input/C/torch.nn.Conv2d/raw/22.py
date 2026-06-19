import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define a Conv2d layer
conv_layer = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=2, padding=1, bias=True)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)