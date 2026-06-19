import torch

# Define the dimensions of the input tensor
batch_size = 2
in_channels = 3
depth = 4
height = 5
width = 6

# Create a random input tensor
input_tensor = torch.randn(batch_size, in_channels, depth, height, width)

# Define the Conv3d layer parameters
out_channels = 8
kernel_size = (2, 3, 4)
stride = (1, 1, 1)
padding = (1, 1, 1)
dilation = (1, 1, 1)
groups = 1
bias = True
padding_mode = 'zeros'

# Create the Conv3d layer
conv3d_layer = torch.nn.Conv3d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias, padding_mode)

# Apply the Conv3d layer to the input tensor
output_tensor = conv3d_layer(input_tensor)

print(output_tensor.shape)