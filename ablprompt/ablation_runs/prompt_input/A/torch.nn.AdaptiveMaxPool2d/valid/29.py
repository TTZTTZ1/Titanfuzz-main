import torch
from torch.nn import AdaptiveMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 56, 56)

# Define the adaptive max pooling layer
pooling_layer = AdaptiveMaxPool2d((7, 7))

# Apply the adaptive max pooling
output_tensor = pooling_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 7, 7])