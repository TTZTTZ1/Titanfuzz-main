import torch
from torch.nn import Conv2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define a Conv2d layer with specific parameters
conv_layer = Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), stride=(2, 2), padding=1, bias=True)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)