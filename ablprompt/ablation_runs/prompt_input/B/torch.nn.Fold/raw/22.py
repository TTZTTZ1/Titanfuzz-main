import torch
from torch.nn import Fold

# Define input dimensions
input_tensor = torch.randn(1, 64, 8, 8)

# Define Fold parameters
kernel_size = 4
stride = 2
padding = 1
dilation = 1

# Create Fold layer
fold = Fold(output_size=(16, 16), kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer to input tensor
output_tensor = fold(input_tensor)

print(output_tensor.shape)