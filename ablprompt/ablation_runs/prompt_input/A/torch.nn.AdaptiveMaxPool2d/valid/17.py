import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 5, 7)
input_tensor = torch.randn(1, 3, 5, 7)

# Define an AdaptiveMaxPool2d layer with output size (2, 2)
adaptive_max_pool = nn.AdaptiveMaxPool2d((2, 2))

# Apply the adaptive max pooling to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 2, 2])