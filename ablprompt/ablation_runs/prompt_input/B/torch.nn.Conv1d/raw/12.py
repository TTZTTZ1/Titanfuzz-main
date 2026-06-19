import torch
import torch.nn as nn

# Create a Conv1d layer
conv1d = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=1, bias=True, padding_mode='zeros')

# Generate random input tensor
input_tensor = torch.randn(20, 16, 50)

# Perform forward pass
output_tensor = conv1d(input_tensor)

print(output_tensor.shape)  # Expected output shape: (20, 33, 25)