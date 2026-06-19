import torch
import torch.nn as nn

# Create a random input tensor with shape (1, 3, 16, 16)
input_tensor = torch.randn(1, 3, 16, 16)

# Define AdaptiveAvgPool2d with output size (8, 8)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((8, 8))

# Apply the adaptive average pooling
output_tensor = adaptive_avg_pool(input_tensor)

print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)