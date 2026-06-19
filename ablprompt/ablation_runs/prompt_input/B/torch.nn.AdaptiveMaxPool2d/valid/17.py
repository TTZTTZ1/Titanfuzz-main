import torch
import torch.nn as nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 20, 20)

# Create an AdaptiveMaxPool2d layer with output size (10, 10)
max_pool = nn.AdaptiveMaxPool2d((10, 10))

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 10, 10])