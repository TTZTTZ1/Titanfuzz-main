import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 50)

# Define a Conv1d layer
conv_layer = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: (1, 33, 24)