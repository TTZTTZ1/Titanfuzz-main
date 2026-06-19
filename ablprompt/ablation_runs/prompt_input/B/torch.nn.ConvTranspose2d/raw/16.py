import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32, 32)

# Define the ConvTranspose2d layer
conv_transpose = nn.ConvTranspose2d(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1, bias=True)

# Apply the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)