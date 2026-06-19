import torch
import torch.nn as nn

# Create an instance of FractionalMaxPool2d
m = nn.FractionalMaxPool2d(kernel_size=3, output_size=(13, 12), return_indices=True)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 24, 24)

# Apply the fractional max pooling
output, indices = m(input_tensor)

print("Output:", output.shape)
print("Indices:", indices.shape)