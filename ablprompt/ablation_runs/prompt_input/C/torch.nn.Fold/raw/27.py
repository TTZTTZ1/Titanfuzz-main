import torch
from torch.nn import Fold

# Define input dimensions and parameters
input_tensor = torch.randn(1, 64, 8, 8)  # Example input tensor
output_size = (16, 16)
kernel_size = 2
stride = 2
padding = 0
dilation = 1

# Create a Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)