import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((3, 4))

# Example input tensor with shape (1, 3, 8, 16)
input_tensor = torch.randn(1, 3, 8, 16)

# Apply the AdaptiveAvgPool2d layer
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 3, 4])