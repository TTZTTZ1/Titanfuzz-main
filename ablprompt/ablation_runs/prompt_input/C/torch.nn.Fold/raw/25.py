import torch
from torch.nn import Fold

# Define the input tensor dimensions
input_tensor = torch.randn(1, 4, 64, 64)

# Define the parameters for Fold
output_size = (64, 64)
kernel_size = 8
stride = 8
padding = 0
dilation = 1

# Create a Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Should be [1, 4, 64, 64]