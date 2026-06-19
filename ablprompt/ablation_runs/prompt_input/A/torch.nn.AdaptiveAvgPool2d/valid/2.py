import torch
import torch.nn as nn

# Define an input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Create an AdaptiveAvgPool2d layer with output size (7, 7)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((7, 7))

# Apply the adaptive average pooling to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 7, 7])