import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define the AdaptiveMaxPool2d layer
adaptive_max_pool = nn.AdaptiveMaxPool2d((7, 7))

# Apply the adaptive max pooling to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 7, 7]