import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the average pooling layer
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)

# Apply the average pooling to the input tensor
output_tensor = avg_pool(input_tensor)

print(output_tensor)