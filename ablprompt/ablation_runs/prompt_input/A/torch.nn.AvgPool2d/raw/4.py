import torch
import torch.nn as nn

# Create an instance of AvgPool2d
pool = nn.AvgPool2d(kernel_size=3, stride=1, padding=1)

# Example input tensor
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size, channels, height, width

# Apply the pooling operation
output_tensor = pool(input_tensor)

print(output_tensor)