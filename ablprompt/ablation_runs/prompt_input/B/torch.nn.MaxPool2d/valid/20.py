import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define MaxPool2d layer with custom parameters
max_pool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1, dilation=1, return_indices=False, ceil_mode=False)

# Apply MaxPool2d to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)