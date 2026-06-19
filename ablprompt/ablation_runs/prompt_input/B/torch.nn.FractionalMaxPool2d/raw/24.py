import torch
from torch import nn

# Create an input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=2, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the layer to the input tensor
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor:", output_tensor.shape)
print("Indices:", indices.shape)