import torch
import torch.nn as nn

# Create a dummy input tensor of shape (1, 16, 32, 32, 32)
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define a Conv3d layer
conv_layer = nn.Conv3d(in_channels=16, out_channels=8, kernel_size=3, stride=1, padding=1)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 8, 32, 32, 32)