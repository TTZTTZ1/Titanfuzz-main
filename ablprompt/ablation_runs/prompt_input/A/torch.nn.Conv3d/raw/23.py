import torch
from torch import nn

# Define a simple 3D convolutional layer
conv_layer = nn.Conv3d(in_channels=1, out_channels=64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Create a dummy input tensor
input_tensor = torch.randn(1, 1, 32, 32, 32)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)