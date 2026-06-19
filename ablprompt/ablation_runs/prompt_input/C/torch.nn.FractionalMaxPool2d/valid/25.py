import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the FractionalMaxPool2d layer
fm_pool = FractionalMaxPool2d(kernel_size=3, output_size=(16, 16), return_indices=True)

# Apply the layer to the input tensor
output_tensor, indices = fm_pool(input_tensor)

print("Output Tensor:", output_tensor.shape)
print("Indices Tensor:", indices.shape)