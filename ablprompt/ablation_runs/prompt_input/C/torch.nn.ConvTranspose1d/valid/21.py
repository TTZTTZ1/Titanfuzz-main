import torch
import torch.nn as nn

# Create a ConvTranspose1d layer
upsample = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(1, 16, 10)

# Perform the transpose convolution
output_tensor = upsample(input_tensor)

print(output_tensor.shape)