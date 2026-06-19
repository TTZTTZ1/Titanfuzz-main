import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (1, 1)
pool = nn.AdaptiveMaxPool2d((1, 1))

# Create a random input tensor of shape (1, 3, 5, 7)
input_tensor = torch.randn(1, 3, 5, 7)

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Expected output: torch.Size([1, 3, 1, 1])