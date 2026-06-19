import torch
import torch.nn as nn

# Define input tensor and parameters for Fold
input_tensor = torch.randn(1, 32, 8, 8)
output_size = (4, 4)
kernel_size = (2, 2)
dilation = (1, 1)
padding = (0, 0)
stride = (2, 2)

# Create a Fold layer
fold_layer = nn.Fold(output_size, kernel_size, dilation=dilation, padding=padding, stride=stride)

# Apply the Fold operation
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)