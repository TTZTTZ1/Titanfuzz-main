import torch
from torch.nn import ConvTranspose2d

# Define input tensor
input_tensor = torch.randn(1, 16, 32, 32)

# Create a ConvTranspose2d layer
conv_transpose_layer = ConvTranspose2d(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)  # Should be [1, 8, 64, 64]