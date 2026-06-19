import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size 7x7
pool = nn.AdaptiveAvgPool2d((7, 7))

# Create a random input tensor with shape (1, 3, 16, 16)
input_tensor = torch.randn(1, 3, 16, 16)

# Apply the pool layer to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 7, 7])