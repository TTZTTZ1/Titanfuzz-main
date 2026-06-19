import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the layer to the input tensor
output, indices = fractional_max_pool(input_tensor)

print("Output shape:", output.shape)
print("Indices shape:", indices.shape)