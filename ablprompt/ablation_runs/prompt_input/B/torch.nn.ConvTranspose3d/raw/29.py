import torch
from torch.nn import ConvTranspose3d

# Define the input tensor
input_tensor = torch.randn(1, 3, 8, 16, 32)

# Create an instance of ConvTranspose3d
conv_transpose_3d = ConvTranspose3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1), output_padding=(0, 0, 0))

# Perform the forward pass
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)