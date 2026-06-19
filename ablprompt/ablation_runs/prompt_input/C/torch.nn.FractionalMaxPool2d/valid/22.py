import torch
import torch.nn as nn

# Define the FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(13, 12), return_indices=True)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Apply the FractionalMaxPool2d layer
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)