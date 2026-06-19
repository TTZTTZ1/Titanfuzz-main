import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Define the ConvTranspose3d layer
conv_transpose_3d = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1), output_padding=(0, 0, 0))

# Apply the ConvTranspose3d layer to the input tensor
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)  # Should be [1, 33, 20, 102, 202]