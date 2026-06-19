import torch
from torch import nn

# Define the Conv1d layer
conv_layer = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([20, 33, 25])