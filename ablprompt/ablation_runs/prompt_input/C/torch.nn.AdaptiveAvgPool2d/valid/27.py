import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 3)
pool = nn.AdaptiveAvgPool2d((3, 3))

# Create a random input tensor with shape (1, 64, 128, 128)
input_tensor = torch.randn(1, 64, 128, 128)

# Apply the pool layer to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 64, 3, 3])