import torch
from torch.nn import ConvTranspose1d

# Define the input tensor
input_tensor = torch.randn(1, 16, 32)

# Create an instance of ConvTranspose1d
conv_transpose = ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

# Apply the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)  # Output should be (1, 8, 65)