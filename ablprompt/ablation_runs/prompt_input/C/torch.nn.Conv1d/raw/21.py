import torch
import torch.nn as nn

# Create a Conv1d layer with specific parameters
conv1d_layer = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=3, stride=2, padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')

# Example input tensor
input_tensor = torch.randn(10, 16, 50)  # Batch size 10, 16 input channels, sequence length 50

# Apply the Conv1d layer to the input tensor
output_tensor = conv1d_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: (10, 32, 24)