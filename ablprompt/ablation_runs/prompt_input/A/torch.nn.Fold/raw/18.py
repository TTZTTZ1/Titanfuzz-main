import torch
from torch.nn import Fold

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 64, 64)  # Example input tensor of shape (batch_size, channels, height, width)
output_size = (16, 16)  # Desired output size after folding
kernel_size = (8, 8)  # Size of each kernel
stride = (4, 4)  # Stride between kernels
padding = (0, 0)  # Padding added to the input

# Create a Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply Fold to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)