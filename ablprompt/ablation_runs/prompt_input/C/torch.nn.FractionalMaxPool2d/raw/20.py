import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define FractionalMaxPool2d layer with specific parameters
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(16, 16), return_indices=True)

# Apply the fractional max pooling operation
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor Shape:", output_tensor.shape)
print("Indices Tensor Shape:", indices.shape)