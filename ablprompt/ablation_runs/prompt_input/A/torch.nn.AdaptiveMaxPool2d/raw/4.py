import torch
import torch.nn as nn

# Define an input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Create an AdaptiveMaxPool2d layer with output size (7, 7)
adaptive_max_pool = nn.AdaptiveMaxPool2d((7, 7))

# Apply the adaptive max pooling to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 7, 7])