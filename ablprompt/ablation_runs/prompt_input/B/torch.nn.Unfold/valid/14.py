import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 3, 8, 8)

# Define the parameters for Unfold
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Initialize the Unfold layer
unfold = Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Unfold operation
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape should be (1, 9, 25)