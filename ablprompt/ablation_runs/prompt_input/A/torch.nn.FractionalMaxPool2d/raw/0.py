import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d layer
fractional_maxpool = nn.FractionalMaxPool2d(
    output_size=(16, 16),
    fractional_stride=(0.5, 0.5),
    padding=0,
    ceil_mode=False
)

# Apply the layer to the input tensor
output_tensor = fractional_maxpool(input_tensor)

print(output_tensor.shape)