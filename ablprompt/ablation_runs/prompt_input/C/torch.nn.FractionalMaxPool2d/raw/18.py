import torch
from torch import nn

# Create an instance of FractionalMaxPool2d
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(13, 12), return_indices=True)

# Generate a random input tensor
input_tensor = torch.randn(1, 3, 24, 24)

# Apply the fractional max pooling operation
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor:", output_tensor.shape)
print("Indices:", indices.shape)