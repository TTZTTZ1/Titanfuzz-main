import torch
import torch.nn as nn

# Create an instance of MaxPool2d
max_pool = nn.MaxPool2d(kernel_size=3, stride=1, padding=0)

# Example input tensor
input_tensor = torch.randn(1, 1, 5, 5)  # Batch size, channels, height, width

# Apply max pooling
output_tensor = max_pool(input_tensor)

print(output_tensor)