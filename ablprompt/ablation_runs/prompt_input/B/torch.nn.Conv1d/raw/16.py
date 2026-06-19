import torch
from torch.nn import Conv1d

# Define the convolutional layer
conv = Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Perform the convolution
output_tensor = conv(input_tensor)

print(output_tensor.shape)  # Expected shape: (20, 33, 24)