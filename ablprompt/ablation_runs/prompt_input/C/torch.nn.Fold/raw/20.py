import torch
from torch.nn import Fold

# Define the input tensor dimensions
input_tensor = torch.randn(1, 64, 8, 8)

# Define the Fold parameters
kernel_size = 3
stride = 1
padding = 1
output_size = (8, 8)

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)