import torch
from torch.nn import Fold

# Define input parameters
input_tensor = torch.randn(1, 3 * 4 * 4, 64)
output_size = (8, 8)
kernel_size = 4
stride = 2
padding = 1
dilation = 1

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 3, 8, 8])