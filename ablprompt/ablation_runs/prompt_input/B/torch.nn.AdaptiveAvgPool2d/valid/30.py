import torch
import torch.nn as nn

# Define a random input tensor with batch size 2, 3 channels, height 8, and width 6
input_tensor = torch.randn(2, 3, 8, 6)

# Create an AdaptiveAvgPool2d layer with output size 4x4
adaptive_avg_pool = nn.AdaptiveAvgPool2d((4, 4))

# Apply the adaptive average pooling to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([2, 3, 4, 4])