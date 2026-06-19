import torch
from torch.nn import Fold

# Example input tensor
input_tensor = torch.randn(1, 96, 8)

# Define the Fold parameters
output_size = (4, 4)
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create a Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 96, 4, 4])