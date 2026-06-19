import torch
from torch.nn import Fold

# Define the input tensor dimensions
input_tensor = torch.randn(1, 96, 8, 8)

# Define the parameters for Fold
output_size = (16, 16)
kernel_size = 3
dilation = 1
padding = 1
stride = 1

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, dilation=dilation, padding=padding, stride=stride)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Should be (1, 96, 16, 16)