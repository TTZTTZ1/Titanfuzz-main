import torch
from torch import nn

# Define an input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Create an instance of AvgPool2d
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Apply the average pooling operation
output_tensor = avg_pool(input_tensor)

print(output_tensor)