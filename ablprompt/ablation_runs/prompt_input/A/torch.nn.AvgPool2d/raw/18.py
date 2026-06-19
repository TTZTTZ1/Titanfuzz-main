import torch
import torch.nn as nn

# Create an instance of AvgPool2d
pool = nn.AvgPool2d(kernel_size=2, stride=1, padding=0)

# Define a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor)