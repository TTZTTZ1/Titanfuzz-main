import torch
import torch.nn as nn

# Define a random tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Create an instance of MaxPool3d
max_pool = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the max pooling operation
output_tensor = max_pool(input_tensor)

print(output_tensor.shape)