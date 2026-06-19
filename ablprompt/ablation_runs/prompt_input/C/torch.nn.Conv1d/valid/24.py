import torch
from torch import nn

# Define the Conv1d layer
conv = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Perform the convolution
output_tensor = conv(input_tensor)

print(output_tensor.shape)  # Expected output shape: (20, 33, 24)