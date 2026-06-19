import torch
from torch.nn import FractionalMaxPool2d

# Define the input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Create an instance of FractionalMaxPool2d with specific parameters
fractional_max_pool = FractionalMaxPool2d(kernel_size=3, output_size=(32, 32), return_indices=True)

# Apply the fractional max pooling operation
output, indices = fractional_max_pool(input_tensor)

print("Output shape:", output.shape)
print("Indices shape:", indices.shape)