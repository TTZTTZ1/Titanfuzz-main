import torch
import torch.nn as nn

# Define the input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Create an instance of FractionalMaxPool2d
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(32, 32), return_indices=True)

# Apply the fractional max pooling
output, indices = fractional_max_pool(input_tensor)

print("Output Shape:", output.shape)
print("Indices Shape:", indices.shape)