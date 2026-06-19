import torch
import torch.nn as nn

# Define input tensor and convolution parameters
input_tensor = torch.randn(1, 3, 4, 5, 6)  # Batch size=1, in_channels=3, spatial dimensions=4x5x6
kernel_size = (2, 3, 4)
stride = (1, 2, 3)

# Create ConvTranspose3d layer
conv_transpose_layer = nn.ConvTranspose3d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride)

# Perform forward pass
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)  # Output shape should reflect the transposed dimensions based on kernel_size and stride