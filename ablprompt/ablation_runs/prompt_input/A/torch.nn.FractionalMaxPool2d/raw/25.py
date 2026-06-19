import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the fractional max pooling layer
fractional_max_pool = FractionalMaxPool2d(output_size=(32, 32), fraction_of_input=0.5)

# Apply the fractional max pooling
output_tensor = fractional_max_pool(input_tensor)

print(output_tensor.shape)