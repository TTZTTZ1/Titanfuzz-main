import torch
from torch.nn import ConvTranspose3d

# Define the input tensor
input_tensor = torch.randn(1, 16, 10, 50, 100)

# Create an instance of ConvTranspose3d
conv_transpose_3d = ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)

# Apply the convolutional transpose operation
output_tensor = conv_transpose_3d(input_tensor)

print(output_tensor.shape)  # Should print the shape after upsampling