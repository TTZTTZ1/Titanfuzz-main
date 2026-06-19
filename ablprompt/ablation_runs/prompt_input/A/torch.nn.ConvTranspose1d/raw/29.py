import torch

# Define input tensor and convolutional transpose layer parameters
input_tensor = torch.randn(1, 3, 10)  # Batch size 1, 3 channels, 10 time steps
kernel_size = 4
stride = 2
padding = 1

# Create a ConvTranspose1d layer
conv_transpose_layer = torch.nn.ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding)

# Perform the forward pass
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor)