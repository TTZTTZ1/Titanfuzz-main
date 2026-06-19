import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 3)
m = nn.AdaptiveMaxPool2d((3, 3))

# Define a random input tensor with shape (1, 64, 8, 9)
input_tensor = torch.randn(1, 64, 8, 9)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = m(input_tensor)

print(output_tensor.shape)  # Expected output shape: (1, 64, 3, 3)