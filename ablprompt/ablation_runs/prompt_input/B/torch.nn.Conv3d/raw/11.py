import torch
import torch.nn as nn

# Define a simple 3D convolutional layer
conv_layer = nn.Conv3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), groups=1, bias=True, padding_mode='zeros')

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)