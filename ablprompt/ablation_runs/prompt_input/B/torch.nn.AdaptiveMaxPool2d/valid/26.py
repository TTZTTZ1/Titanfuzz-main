import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
m = nn.AdaptiveMaxPool2d((3, 3))

# Generate a random input tensor of shape (2, 16, 10, 12)
input_tensor = torch.randn(2, 16, 10, 12)

# Apply the AdaptiveMaxPool2d layer
output_tensor = m(input_tensor)

print(output_tensor.shape)  # Expected output shape: (2, 16, 3, 3)