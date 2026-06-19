import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define the AvgPool2d layer
avg_pool = nn.AvgPool2d(kernel_size=5, stride=2, padding=1, ceil_mode=True, count_include_pad=False, divisor_override=None)

# Apply the AvgPool2d layer to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor.shape)