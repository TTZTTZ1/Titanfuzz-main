import torch
from torch.nn import Conv3d

# Define input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define Conv3d layer
conv_layer = Conv3d(in_channels=3, out_channels=8, kernel_size=(2, 2, 2), stride=(1, 1, 1), padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')

# Apply convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)