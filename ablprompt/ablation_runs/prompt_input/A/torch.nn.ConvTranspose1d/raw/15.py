import torch

# Define input tensor and convolutional transpose parameters
input_tensor = torch.randn(1, 3, 5)  # Batch size of 1, 3 input channels, sequence length of 5
kernel_size = 3
stride = 2
output_padding = 1

# Create a ConvTranspose1d layer
conv_transpose_layer = torch.nn.ConvTranspose1d(in_channels=3, out_channels=6, kernel_size=kernel_size, stride=stride, output_padding=output_padding)

# Perform the forward pass
output_tensor = conv_transpose_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)