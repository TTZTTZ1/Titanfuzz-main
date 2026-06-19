import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the parameters for Unfold
kernel_size = (2, 2)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Create an instance of Unfold
unfold = Unfold(kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 9, 16])