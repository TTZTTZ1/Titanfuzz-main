import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the FractionalMaxPool2d layer
fm_pool = FractionalMaxPool2d(kernel_size=3, output_size=(8, 8), return_indices=True)

# Apply the fractional max pooling
output, indices = fm_pool(input_tensor)

print("Output shape:", output.shape)
print("Indices shape:", indices.shape)