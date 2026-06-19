import torch
from torch.nn import Fold

# Example input tensor
input_tensor = torch.randn(1, 64, 8, 8)

# Define the Fold layer
output_size = (16, 16)
kernel_size = 4
stride = 2
padding = 1
dilation = 1
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 64, 16, 16])