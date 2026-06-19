import torch
from torch.nn import AdaptiveMaxPool2d

# Create a random input tensor
input_tensor = torch.randn(1, 3, 16, 16)

# Define the adaptive max pooling layer
pool = AdaptiveMaxPool2d((8, 8))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 8, 8]