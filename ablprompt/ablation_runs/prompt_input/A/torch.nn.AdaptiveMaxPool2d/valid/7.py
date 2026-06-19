import torch
import torch.nn as nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 56, 56)

# Create an AdaptiveMaxPool2d layer with output size (7, 7)
pool = nn.AdaptiveMaxPool2d((7, 7))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 7, 7])