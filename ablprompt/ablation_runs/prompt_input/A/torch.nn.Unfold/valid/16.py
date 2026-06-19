import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define the kernel size and stride for Unfold
kernel_size = (2, 2)
stride = (1, 1)

# Create an instance of Unfold
unfold = nn.Unfold(kernel_size=kernel_size, stride=stride)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape will depend on the input dimensions and parameters