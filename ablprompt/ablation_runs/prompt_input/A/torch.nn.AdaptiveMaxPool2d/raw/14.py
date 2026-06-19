import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 64, 64)
input_tensor = torch.randn(1, 3, 64, 64)

# Define the AdaptiveMaxPool2d layer with output size (8, 8)
adaptive_max_pool = nn.AdaptiveMaxPool2d((8, 8))

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 8, 8])