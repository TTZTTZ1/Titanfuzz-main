import torch
import torch.nn as nn

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 4, 8, 8)
output_size = (2, 2)
kernel_size = 2
stride = 2
padding = 0
dilation = 1

# Create a Fold layer
fold_layer = nn.Fold(output_size, kernel_size, stride, padding, dilation)

# Apply Fold to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)