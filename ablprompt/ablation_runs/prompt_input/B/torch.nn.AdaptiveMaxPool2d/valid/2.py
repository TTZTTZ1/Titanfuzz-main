import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 4)
adaptive_max_pool = nn.AdaptiveMaxPool2d((3, 4))

# Create a random input tensor with shape (2, 5, 8, 9)
input_tensor = torch.randn(2, 5, 8, 9)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: (2, 5, 3, 4)