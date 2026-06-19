import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
max_pool = nn.AdaptiveMaxPool2d((3, 3))

# Create a random input tensor of shape (1, 1, 8, 9)
input_tensor = torch.randn(1, 1, 8, 9)

# Apply the AdaptiveMaxPool2d layer
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 1, 3, 3])