import torch
import torch.nn as nn

# Create a ConvTranspose2d layer
m = nn.ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1))

# Create a random input tensor
input_tensor = torch.randn(1, 32, 32, 32)

# Perform the transposed convolution
output_tensor = m(input_tensor)

print(output_tensor.shape)