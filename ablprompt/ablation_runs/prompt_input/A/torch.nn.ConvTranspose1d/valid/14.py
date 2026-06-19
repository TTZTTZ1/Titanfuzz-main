import torch

# Define input tensor and convolutional transpose parameters
input_tensor = torch.randn(1, 3, 10)  # Batch size=1, in_channels=3, sequence length=10
out_channels = 6
kernel_size = 5
stride = 2
padding = 1

# Create an instance of ConvTranspose1d
conv_transpose = torch.nn.ConvTranspose1d(in_channels=3, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding)

# Perform the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)