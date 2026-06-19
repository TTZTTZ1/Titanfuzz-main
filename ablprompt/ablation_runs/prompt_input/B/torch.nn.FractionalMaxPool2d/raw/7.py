import torch
from torch.nn import FractionalMaxPool2d

# Define input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Create FractionalMaxPool2d layer
fm_pool = FractionalMaxPool2d(kernel_size=3, output_size=(16, 16), return_indices=True)

# Apply the layer to the input tensor
output, indices = fm_pool(input_tensor)

print("Output:", output.shape)
print("Indices:", indices.shape)