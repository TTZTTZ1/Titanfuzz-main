import torch

# Define input tensor and parameters for ConvTranspose1d
input_tensor = torch.randn(1, 3, 5)  # Batch size=1, in_channels=3, sequence_length=5
out_channels = 6
kernel_size = 3
stride = 2
padding = 1

# Create an instance of ConvTranspose1d
conv_transpose1d = torch.nn.ConvTranspose1d(in_channels=3, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the convolutional transpose operation
output_tensor = conv_transpose1d(input_tensor)

print(output_tensor)