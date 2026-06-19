import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Define the kernel size and stride for unfold
kernel_size = (2, 2)
stride = (1, 1)

# Initialize the Unfold layer
unfold = Unfold(kernel_size=kernel_size, stride=stride)

# Apply the Unfold operation
output_tensor = unfold(input_tensor)

print(output_tensor)