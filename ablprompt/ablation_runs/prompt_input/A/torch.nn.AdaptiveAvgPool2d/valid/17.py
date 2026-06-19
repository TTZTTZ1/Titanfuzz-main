import torch
from torch import nn

# Create a random input tensor of shape (1, 3, 20, 20)
input_tensor = torch.randn(1, 3, 20, 20)

# Define an AdaptiveAvgPool2d layer with output size (5, 5)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((5, 5))

# Apply the adaptive average pooling to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Expected output: torch.Size([1, 3, 5, 5])