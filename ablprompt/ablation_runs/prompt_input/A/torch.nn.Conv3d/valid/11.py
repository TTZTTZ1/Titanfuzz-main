import torch

# Define input tensor and convolutional layer parameters
input_tensor = torch.randn(1, 3, 4, 4, 4)  # Batch size of 1, 3 channels, 4x4x4 spatial dimensions
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=6, kernel_size=2, stride=1, padding=0)

# Perform convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)