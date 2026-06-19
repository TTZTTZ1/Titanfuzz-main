import torch
import torch.nn as nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Create an AdaptiveAvgPool2d layer with output size (8, 8)
pool = nn.AdaptiveAvgPool2d((8, 8))

# Apply the pool layer to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 8, 8])