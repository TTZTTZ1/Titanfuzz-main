import torch
from torch.nn import ConvTranspose1d

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32)

# Define the ConvTranspose1d layer
upsample = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Apply the transposed convolution
output_tensor = upsample(input_tensor)

print(output_tensor.shape)  # Should be [1, 8, 65]