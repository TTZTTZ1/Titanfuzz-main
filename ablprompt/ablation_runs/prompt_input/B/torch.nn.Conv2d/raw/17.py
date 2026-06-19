import torch
from torch.nn import Conv2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define a Conv2d layer
conv_layer = Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1, bias=True)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)