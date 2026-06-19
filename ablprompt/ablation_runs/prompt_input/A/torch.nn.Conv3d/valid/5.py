import torch
import torch.nn as nn

# Define a simple 3D convolutional layer
conv_layer = nn.Conv3d(in_channels=1, out_channels=16, kernel_size=(3, 3, 3), stride=1, padding=1)

# Create a dummy input tensor (batch size of 1, 1 channel, 32x32x32)
input_tensor = torch.randn(1, 1, 32, 32, 32)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 16, 32, 32, 32]