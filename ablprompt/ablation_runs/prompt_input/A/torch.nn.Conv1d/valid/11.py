import torch
from torch import nn

# Define a simple 1D convolutional layer
conv_layer = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=2)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 100)  # Batch size of 1, 3 channels, sequence length of 100

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)