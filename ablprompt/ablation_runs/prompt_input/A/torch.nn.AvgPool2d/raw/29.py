import torch
import torch.nn as nn

# Create an instance of AvgPool2d
avg_pool = nn.AvgPool2d(kernel_size=3, stride=1, padding=1)

# Define a random input tensor
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size 1, 3 channels, 5x5 spatial dimensions

# Apply the average pooling operation
output_tensor = avg_pool(input_tensor)

print(output_tensor)