import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the fractional max pooling layer
fractional_max_pool = FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the fractional max pooling
output, indices = fractional_max_pool(input_tensor)

print("Output:", output.shape)
print("Indices:", indices.shape)