import torch
from torch.nn import Conv3d

# Create a random input tensor with shape (batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 3, 32, 64, 64)

# Define the Conv3d layer with specific parameters
conv_layer = Conv3d(in_channels=3, out_channels=16, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=True)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 16, 32, 64, 64)