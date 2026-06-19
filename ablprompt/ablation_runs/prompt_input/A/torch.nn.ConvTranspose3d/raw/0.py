import torch
from torch.nn import ConvTranspose3d

# Define input tensor and parameters for ConvTranspose3d
input_tensor = torch.randn(1, 3, 64, 64, 64)
kernel_size = (3, 3, 3)
stride = (2, 2, 2)
padding = (1, 1, 1)

# Create an instance of ConvTranspose3d
conv_transpose3d_layer = ConvTranspose3d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the layer to the input tensor
output_tensor = conv_transpose3d_layer(input_tensor)

print(output_tensor.shape)