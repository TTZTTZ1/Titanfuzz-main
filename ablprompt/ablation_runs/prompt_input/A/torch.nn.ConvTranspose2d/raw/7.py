import torch

# Define input tensor and parameters for ConvTranspose2d
input_tensor = torch.randn(1, 3, 64, 64)  # Batch size of 1, 3 channels, 64x64 image
kernel_size = 5
stride = 2
padding = 0
output_padding = 1

# Create an instance of ConvTranspose2d
conv_transpose = torch.nn.ConvTranspose2d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding, output_padding=output_padding)

# Apply the convolutional transpose operation
output_tensor = conv_transpose(input_tensor)

print(output_tensor.shape)