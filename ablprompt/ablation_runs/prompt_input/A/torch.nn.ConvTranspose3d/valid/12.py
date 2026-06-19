import torch
from torch.nn import ConvTranspose3d

# Define input tensor and parameters for ConvTranspose3d
input_tensor = torch.randn(1, 16, 8, 8, 8)
kernel_size = (3, 3, 3)
stride = (2, 2, 2)
padding = (1, 1, 1)

# Create an instance of ConvTranspose3d
conv_transpose3d = ConvTranspose3d(in_channels=16, out_channels=8, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the convolutional transpose operation
output_tensor = conv_transpose3d(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 8, 15, 15, 15]