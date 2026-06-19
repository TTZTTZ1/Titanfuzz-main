import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 10, 10)

# Define the fractional max pooling layer
fractional_max_pool = FractionalMaxPool2d(output_size=(5, 5), fractional_stride=(2, 2), padding=1)

# Apply the fractional max pooling to the input tensor
output_tensor = fractional_max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)