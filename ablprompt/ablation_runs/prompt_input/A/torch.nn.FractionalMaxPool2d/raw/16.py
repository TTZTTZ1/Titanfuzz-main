import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define FractionalMaxPool2d layer
fractional_maxpool = nn.FractionalMaxPool2d(output_size=(8, 8), fractional_stride=(0.5, 0.5))

# Apply the FractionalMaxPool2d layer to the input tensor
output_tensor = fractional_maxpool(input_tensor)

print(output_tensor.shape)