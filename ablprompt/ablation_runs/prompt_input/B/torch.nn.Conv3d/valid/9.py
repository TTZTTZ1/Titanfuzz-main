import torch

# Define input tensor dimensions
batch_size = 2
in_channels = 3
out_channels = 16
depth = 5
height = 7
width = 9

# Create random input tensor
input_tensor = torch.randn(batch_size, in_channels, depth, height, width)

# Create Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=in_channels, out_channels=out_channels, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)