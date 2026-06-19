import torch
import torch.nn as nn

# Define the input tensor dimensions
input_tensor = torch.randn(1, 96, 8, 8)  # Batch size=1, Channels=96, Height=8, Width=8

# Define the Fold layer parameters
output_size = (16, 16)
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)

# Create the Fold layer
fold_layer = nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)