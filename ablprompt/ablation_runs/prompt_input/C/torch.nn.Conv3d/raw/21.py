import torch
from torch.nn import Conv3d

# Define the input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Create a 3D convolution layer
conv_layer = Conv3d(in_channels=3, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the convolution layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)