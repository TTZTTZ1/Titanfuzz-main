import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the fractional max pooling parameters
output_size = (32, 32)
fractional_stride = (0.5, 0.5)
padding = (0, 0)
ceil_mode = False

# Apply fractional max pooling
fractional_max_pool = FractionalMaxPool2d(output_size=output_size, fractional_stride=fractional_stride, padding=padding, ceil_mode=ceil_mode)
output_tensor = fractional_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)