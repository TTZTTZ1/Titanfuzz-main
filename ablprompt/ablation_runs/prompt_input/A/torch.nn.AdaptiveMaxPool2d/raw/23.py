import torch
from torch.nn import AdaptiveMaxPool2d

# Create a random input tensor of shape (1, 3, 64, 64)
input_tensor = torch.randn(1, 3, 64, 64)

# Define the adaptive max pooling layer to reduce the spatial dimensions to (8, 8)
pooling_layer = AdaptiveMaxPool2d((8, 8))

# Apply the adaptive max pooling layer to the input tensor
output_tensor = pooling_layer(input_tensor)

print(output_tensor.shape)  # Expected output: torch.Size([1, 3, 8, 8])