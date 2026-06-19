import torch
from torch.nn import Conv3d

# Define the input tensor dimensions
batch_size = 2
in_channels = 3
out_channels = 64
depth = 32
height = 32
width = 32

# Create a random input tensor
input_tensor = torch.randn(batch_size, in_channels, depth, height, width)

# Define the Conv3d layer
conv_layer = Conv3d(in_channels=in_channels,
                    out_channels=out_channels,
                    kernel_size=(3, 3, 3),
                    stride=(1, 1, 1),
                    padding=(1, 1, 1),
                    bias=True)

# Apply the convolution operation
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)