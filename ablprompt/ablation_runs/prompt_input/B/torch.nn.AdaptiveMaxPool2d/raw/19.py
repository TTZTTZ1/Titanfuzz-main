import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
m = nn.AdaptiveMaxPool2d((3, 3))

# Create a random input tensor of shape (1, 1, 10, 10)
input_tensor = torch.randn(1, 1, 10, 10)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = m(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 1, 3, 3])