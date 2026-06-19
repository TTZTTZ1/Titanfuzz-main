import torch
import torch.nn as nn

# Define a simple Conv1d layer
conv_layer = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256)  # Batch size of 1, 3 input channels, sequence length of 256

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)