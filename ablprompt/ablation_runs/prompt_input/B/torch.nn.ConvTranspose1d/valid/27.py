import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define the ConvTranspose1d layer
upsample = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros')

# Apply the layer to the input tensor
output_tensor = upsample(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 8, 65])