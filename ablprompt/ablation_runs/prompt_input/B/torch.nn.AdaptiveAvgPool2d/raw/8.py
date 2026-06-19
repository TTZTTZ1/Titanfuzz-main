import torch
from torch import nn

# Create an AdaptiveAvgPool2d layer with output size (3, 3)
pool = nn.AdaptiveAvgPool2d((3, 3))

# Create a random input tensor with shape (1, 4, 6, 8)
input_tensor = torch.randn(1, 4, 6, 8)

# Apply the adaptive average pooling
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: (1, 4, 3, 3)