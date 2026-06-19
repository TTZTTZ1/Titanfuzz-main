import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the FractionalMaxPool2d layer to the input tensor
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor:", output_tensor)
print("Indices:", indices)