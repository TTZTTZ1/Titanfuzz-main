import torch
import torch.nn as nn

# Define an input tensor
input_tensor = torch.randn(1, 3, 24, 24)

# Create an AdaptiveMaxPool2d layer with output size (6, 6)
pool = nn.AdaptiveMaxPool2d((6, 6))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 6, 6])