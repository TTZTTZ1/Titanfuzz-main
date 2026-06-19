import torch
from torch.nn import Unfold

# Define input tensor and parameters for Unfold
input_tensor = torch.randn(1, 3, 4, 4)
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)

# Create an instance of Unfold
unfold = Unfold(kernel_size=kernel_size, stride=stride, padding=padding)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Output shape should be [1, 12, 3, 3]