import torch
from torch.nn import AdaptiveAvgPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define the adaptive average pooling layer
output_size = (16, 16)
adaptive_avg_pool = AdaptiveAvgPool2d(output_size)

# Apply the adaptive average pooling to the input tensor
pooled_output = adaptive_avg_pool(input_tensor)

print(pooled_output.shape)  # Output should be [1, 3, 16, 16]