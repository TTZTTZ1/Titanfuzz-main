import torch
from torch.nn import ConvTranspose2d

# Define input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define convolutional transpose layer
conv_transpose_layer = ConvTranspose2d(in_channels=3, out_channels=6, kernel_size=3, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)