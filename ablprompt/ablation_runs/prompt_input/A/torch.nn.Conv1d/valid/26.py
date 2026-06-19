import torch
from torch import nn

# Define a simple Conv1d layer
conv_layer = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=2)

# Create a random input tensor of shape (batch_size, in_channels, sequence_length)
input_tensor = torch.randn(10, 3, 100)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (batch_size, out_channels, output_sequence_length)