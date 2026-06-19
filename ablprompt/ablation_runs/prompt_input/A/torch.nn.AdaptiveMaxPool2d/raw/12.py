import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define AdaptiveMaxPool2d layer with output size (8, 8)
adaptive_max_pool = nn.AdaptiveMaxPool2d((8, 8))

# Apply the adaptive max pooling to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 8, 8])