import torch
import torch.nn as nn

# Create a ConvTranspose2d layer
m = nn.ConvTranspose2d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)

# Generate a random input tensor
input_tensor = torch.randn(20, 16, 50, 100)

# Perform the forward pass
output_tensor = m(input_tensor)

print(output_tensor.shape)