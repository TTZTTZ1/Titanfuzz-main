import torch
from torch.nn import Fold

# Define the input tensor
input_tensor = torch.randn(1, 64, 8, 8)

# Define the Fold parameters
output_size = (16, 16)
kernel_size = (4, 4)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)