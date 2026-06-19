import torch
import torch.nn as nn

# Define the input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Create an instance of FractionalMaxPool2d
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(16, 16), return_indices=True)

# Apply the fractional max pooling
output, indices = fractional_max_pool(input_tensor)

print("Output shape:", output.shape)
print("Indices shape:", indices.shape)