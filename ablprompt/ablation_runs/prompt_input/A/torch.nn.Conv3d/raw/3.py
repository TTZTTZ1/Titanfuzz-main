import torch

# Define input tensor and convolution parameters
input_tensor = torch.randn(1, 3, 4, 4, 4)  # Batch size of 1, 3 channels, 4x4x4 spatial dimensions
weight = torch.randn(9, 3, 2, 2, 2)       # 9 output channels, 3 input channels, 2x2x2 kernel size
bias = torch.randn(9)                     # 9 bias terms for each output channel

# Create a Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=9, kernel_size=(2, 2, 2))

# Apply the convolution operation
output_tensor = conv_layer(input_tensor)

print(output_tensor)