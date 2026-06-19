import torch

# Define input tensor and parameters for ConvTranspose1d
input_tensor = torch.randn(1, 3, 10)  # Batch size of 1, 3 input channels, sequence length of 10
kernel_size = 5
stride = 2
padding = 1
output_padding = 0

# Create an instance of ConvTranspose1d
conv_transpose1d = torch.nn.ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, padding=padding, output_padding=output_padding)

# Perform the convolutional transpose operation
output_tensor = conv_transpose1d(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)