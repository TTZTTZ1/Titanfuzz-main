import torch
from torch import nn

# Create an input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define AdaptiveAvgPool2d layer with output size (7, 7)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((7, 7))

# Apply the AdaptiveAvgPool2d layer to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Output should be [1, 3, 7, 7]