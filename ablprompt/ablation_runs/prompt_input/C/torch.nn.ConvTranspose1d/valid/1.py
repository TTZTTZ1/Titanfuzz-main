import torch
import torch.nn as nn

# Define the ConvTranspose1d layer
upsample = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(1, 16, 5)

# Apply the ConvTranspose1d layer
output_tensor = upsample(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 8, 9])