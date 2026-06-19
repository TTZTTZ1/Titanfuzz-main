import torch
import torch.nn as nn

# Define a simple 1D convolutional layer
conv1d = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=2)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 10)

# Apply the convolutional layer
output_tensor = conv1d(input_tensor)

print(output_tensor.shape)