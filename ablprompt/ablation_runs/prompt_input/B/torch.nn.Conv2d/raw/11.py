import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define a Conv2d layer with specific parameters
conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(5, 5), stride=(2, 2), padding=(1, 1), bias=True)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)