import torch
from torch.nn import Conv3d

# Define input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Create Conv3d layer
conv_layer = Conv3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)