import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d layer
frac_max_pool = nn.FractionalMaxPool2d(kernel_size=(3, 3), output_ratio=(0.5, 0.5))

# Apply the fractional max pooling
output_tensor = frac_max_pool(input_tensor)

print(output_tensor.shape)