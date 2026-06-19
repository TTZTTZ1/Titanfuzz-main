import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define MaxPool2d layer with specific parameters
max_pool_layer = nn.MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, return_indices=True, ceil_mode=False)

# Apply the MaxPool2d layer to the input tensor
output_tensor, indices = max_pool_layer(input_tensor)

print("Output Tensor Shape:", output_tensor.shape)
print("Indices Tensor Shape:", indices.shape)