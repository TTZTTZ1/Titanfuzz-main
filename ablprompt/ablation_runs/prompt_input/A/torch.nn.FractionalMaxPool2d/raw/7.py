import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the fractional max pooling layer
pool = FractionalMaxPool2d(output_size=(8, 8), fractional_stride=(0.5, 0.5))

# Apply the fractional max pooling layer to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)