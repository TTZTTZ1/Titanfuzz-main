import torch
import torch.nn as nn

# Define the ConvTranspose2d layer
conv_transpose2d = nn.ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=True)

# Create a random input tensor
input_tensor = torch.randn(1, 32, 16, 16)

# Perform the forward pass
output_tensor = conv_transpose2d(input_tensor)

print(output_tensor.shape)