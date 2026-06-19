import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 10, 10)

# Define the fractional max pooling parameters
output_size = (5, 5)
fractional_stride = (2, 2)
padding = (1, 1)
ceil_mode = True

# Apply FractionalMaxPool2d
fractional_max_pool = FractionalMaxPool2d(output_size=output_size, fractional_stride=fractional_stride, padding=padding, ceil_mode=ceil_mode)
output_tensor = fractional_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)