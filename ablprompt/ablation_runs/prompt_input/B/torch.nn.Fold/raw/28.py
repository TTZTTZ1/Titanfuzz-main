import torch
from torch.nn import Fold

# Define the input tensor dimensions
input_tensor = torch.randn(1, 96, 7, 7)

# Define the parameters for Fold
output_size = (14, 14)
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 96, 14, 14])