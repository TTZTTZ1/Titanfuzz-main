import torch
from torch.nn import Fold

# Example input dimensions
input_tensor = torch.randn(1, 64, 8, 8)  # Batch size, channels * kernel_size^2, height, width

# Define Fold parameters
kernel_size = 3
output_size = (16, 16)
stride = 2
padding = 1
dilation = 1

# Create Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 64, 16, 16]