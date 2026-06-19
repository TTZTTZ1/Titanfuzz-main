import torch
from torch.nn import Fold

# Define the parameters
output_size = (8, 8)
kernel_size = (3, 3)
dilation = 1
padding = 1
stride = 1

# Create a random input tensor
input_tensor = torch.randn(1, 9, 64)

# Initialize the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, dilation=dilation, padding=padding, stride=stride)

# Apply the Fold layer
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)