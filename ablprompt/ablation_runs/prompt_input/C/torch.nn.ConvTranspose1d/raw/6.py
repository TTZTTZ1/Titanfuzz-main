import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define the ConvTranspose1d layer
upsample = nn.ConvTranspose1d(in_channels=16, out_channels=16, kernel_size=3, stride=2, padding=1)

# Apply the layer to the input tensor
output_tensor = upsample(input_tensor)

print(output_tensor.shape)