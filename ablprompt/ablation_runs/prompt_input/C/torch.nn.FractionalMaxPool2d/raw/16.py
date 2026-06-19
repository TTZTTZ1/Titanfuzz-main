import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the FractionalMaxPool2d layer
fractional_max_pool = FractionalMaxPool2d(kernel_size=2, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the layer to the input tensor
output, indices = fractional_max_pool(input_tensor)

print("Output:", output.shape)
print("Indices:", indices.shape)