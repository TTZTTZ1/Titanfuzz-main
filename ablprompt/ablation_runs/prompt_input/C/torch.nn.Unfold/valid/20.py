import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 8, 8)

# Define Unfold parameters
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)
dilation = (1, 1)

# Apply Unfold
unfold = nn.Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 3*2*2, 7*7]