import torch
import torch.nn as nn

# Create a 1D convolutional layer
conv = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Apply the convolutional layer
output_tensor = conv(input_tensor)

print(output_tensor.shape)  # Expected output shape: (20, 33, 25)