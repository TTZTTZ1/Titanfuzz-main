import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define the Unfold parameters
kernel_size = (3, 3)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Initialize the Unfold layer
unfold = Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 9, 9])