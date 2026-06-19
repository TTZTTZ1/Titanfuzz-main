import torch
import torch.nn as nn

# Create a random input tensor of shape (1, 3, 8, 8)
input_tensor = torch.randn(1, 3, 8, 8)

# Define the AdaptiveAvgPool2d layer with output size (4, 4)
adaptive_avg_pool = nn.AdaptiveAvgPool2d((4, 4))

# Apply the AdaptiveAvgPool2d layer to the input tensor
output_tensor = adaptive_avg_pool(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([1, 3, 4, 4])