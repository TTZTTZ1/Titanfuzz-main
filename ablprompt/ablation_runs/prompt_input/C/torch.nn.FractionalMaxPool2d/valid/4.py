import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define FractionalMaxPool2d layer
fractional_max_pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(128, 128), return_indices=True)

# Apply the layer to the input tensor
output_tensor, indices = fractional_max_pool(input_tensor)

print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)