import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (1, 1)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((1, 1))

# Create a random input tensor of shape (1, 3, 4, 4)
input_tensor = torch.randn(1, 3, 4, 4)

# Apply the AdaptiveAvgPool2d layer to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 1, 1])