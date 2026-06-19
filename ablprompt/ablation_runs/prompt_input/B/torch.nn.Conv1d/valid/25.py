import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 100)

# Define a Conv1d layer
conv_layer = nn.Conv1d(in_channels=3, out_channels=16, kernel_size=5, stride=2, padding=2, groups=1, bias=True, padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 16, 50])