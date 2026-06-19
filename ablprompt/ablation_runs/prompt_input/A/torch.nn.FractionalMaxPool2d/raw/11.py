import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d parameters
output_size = (8, 8)
fractional_stride = (0.5, 0.5)
padding = (0, 0)
ceil_mode = False

# Create an instance of FractionalMaxPool2d
fractional_max_pool = nn.FractionalMaxPool2d(output_size=output_size, fractional_stride=fractional_stride, padding=padding, ceil_mode=ceil_mode)

# Apply the FractionalMaxPool2d to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)