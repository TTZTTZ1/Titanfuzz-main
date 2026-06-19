import torch
from torch.nn import ConvTranspose3d

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define the ConvTranspose3d layer
conv_transpose_layer = ConvTranspose3d(in_channels=16, out_channels=8, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1))

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 8, 64, 64, 64])