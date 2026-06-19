import torch
import torch.nn as nn

# Define an AdaptiveAvgPool2d layer with output size (3, 4)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((3, 4))

# Create a random input tensor with shape (1, 3, 8, 16)
input_tensor = torch.randn(1, 3, 8, 16)

# Apply the adaptive average pooling
output_tensor = adaptive_avg_pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)