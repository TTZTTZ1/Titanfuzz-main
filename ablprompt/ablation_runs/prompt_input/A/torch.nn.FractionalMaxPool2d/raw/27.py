import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(output_size=(32, 32), fractional_stride=(0.5, 0.5))

# Apply the layer to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print(output_tensor.shape)