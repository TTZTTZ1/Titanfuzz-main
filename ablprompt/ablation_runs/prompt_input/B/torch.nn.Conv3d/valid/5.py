import torch
from torch import nn

# Create a random tensor as input
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define a Conv3d layer
conv_layer = nn.Conv3d(in_channels=3, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)