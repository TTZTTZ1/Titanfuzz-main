import torch
from torch.nn import FractionalMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the FractionalMaxPool2d layer
fm_pool = FractionalMaxPool2d(kernel_size=3, output_ratio=(0.5, 0.5), return_indices=True)

# Apply the FractionalMaxPool2d layer
output_tensor, indices = fm_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)