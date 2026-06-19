import torch
import torch.nn as nn

# Define a simple Conv1d layer
conv_layer = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3)

# Create a random input tensor of shape (batch_size, in_channels, sequence_length)
input_tensor = torch.randn(10, 3, 50)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (batch_size, out_channels, new_sequence_length)