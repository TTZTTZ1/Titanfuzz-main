import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define MaxPool2d layer with custom parameters
max_pool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, return_indices=True, ceil_mode=False)

# Apply MaxPool2d to the input tensor
output_tensor, indices = max_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
print("Indices Shape:", indices.shape)