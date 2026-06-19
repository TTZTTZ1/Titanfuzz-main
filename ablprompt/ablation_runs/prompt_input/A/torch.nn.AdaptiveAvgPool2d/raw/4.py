import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define the AdaptiveAvgPool2d layer
output_size = (128, 128)
adaptive_avg_pool = nn.AdaptiveAvgPool2d(output_size)

# Apply the adaptive average pooling
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 128, 128])