import torch
from torch.nn import AdaptiveMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define the adaptive max pooling layer
pool = AdaptiveMaxPool2d((1, 1))

# Apply the adaptive max pooling to the input tensor
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 1, 1]