import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the FractionalMaxPool2d layer
fractional_max_pool = FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5))

# Apply the fractional max pooling
output_tensor = fractional_max_pool(input_tensor)

print(output_tensor.shape)