import torch
from torch import nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 32, 32, 32)

# Create a Conv3d layer
conv_layer = nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)