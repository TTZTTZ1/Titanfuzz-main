import torch
import torch.nn as nn

# Define an input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Create an AdaptiveAvgPool2d layer with output size (16, 16)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((16, 16))

# Apply the adaptive average pooling to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 3, 16, 16])