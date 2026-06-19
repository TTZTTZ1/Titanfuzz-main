import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define a Conv3d layer
conv_layer = nn.Conv3d(in_channels=3, out_channels=8, kernel_size=(2, 3, 4), stride=(1, 1, 1), padding=(1, 1, 1), dilation=(1, 1, 1), groups=1, bias=True, padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)