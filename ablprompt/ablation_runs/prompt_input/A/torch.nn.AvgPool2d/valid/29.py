import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the AvgPool2d layer
pool = nn.AvgPool2d(kernel_size=2, stride=2, padding=0)

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor)