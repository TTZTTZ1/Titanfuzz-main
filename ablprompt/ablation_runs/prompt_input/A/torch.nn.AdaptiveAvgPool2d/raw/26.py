import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 5, 7)
input_tensor = torch.randn(1, 3, 5, 7)

# Define the AdaptiveAvgPool2d layer with output size (2, 2)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((2, 2))

# Apply the AdaptiveAvgPool2d layer to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Output should be torch.Size([1, 3, 2, 2])