import torch
from torch import nn

# Define the ConvTranspose3d layer
m = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, output_padding=1, groups=1, bias=True, dilation=1)

# Create a random input tensor
input_tensor = torch.randn(20, 16, 10, 50, 100)

# Perform the forward pass
output_tensor = m(input_tensor)

print(output_tensor.shape)