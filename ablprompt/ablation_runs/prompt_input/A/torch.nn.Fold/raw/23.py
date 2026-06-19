import torch
import torch.nn as nn

# Define input tensor and parameters for Fold operation
input_tensor = torch.randn(1, 4, 8, 8)  # Example input tensor of shape (batch_size, channels, height, width)
output_channels = 2
kernel_size = 2
stride = 2
padding = 0

# Create a Fold layer
fold_layer = nn.Fold(output_size=(4, 4), kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold operation to the input tensor
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)