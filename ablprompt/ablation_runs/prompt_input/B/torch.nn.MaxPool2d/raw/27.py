import torch
from torch.nn import MaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Define the MaxPool2d layer with custom parameters
max_pool_layer = MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, return_indices=True, ceil_mode=False)

# Apply the MaxPool2d layer to the input tensor
output_tensor, indices = max_pool_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)