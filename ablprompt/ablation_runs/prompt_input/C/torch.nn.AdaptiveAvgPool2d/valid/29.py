import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size 3x3
pool = nn.AdaptiveAvgPool2d((3, 3))

# Generate a random input tensor of shape (1, 4, 8, 8)
input_tensor = torch.randn(1, 4, 8, 8)

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)