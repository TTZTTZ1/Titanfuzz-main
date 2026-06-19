import torch

# Define input tensor and convolutional transpose parameters
input_tensor = torch.randn(1, 3, 20)
kernel_size = 5
stride = 2
padding = 1

# Create an instance of ConvTranspose1d
conv_transpose_layer = torch.nn.ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding)

# Perform the forward pass
output_tensor = conv_transpose_layer(input_tensor)

print(output_tensor.shape)  # Output shape should be (1, 6, 47)