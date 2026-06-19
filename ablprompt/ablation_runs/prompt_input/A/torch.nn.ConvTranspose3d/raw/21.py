import torch
import torch.nn as nn

# Define a simple 3D convolutional transpose layer
conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=1, kernel_size=(3, 3, 3), stride=(2, 2, 2))

# Create a random input tensor of shape (batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 1, 8, 8, 8)

# Apply the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)  # Output should be (1, 1, 15, 17, 17)