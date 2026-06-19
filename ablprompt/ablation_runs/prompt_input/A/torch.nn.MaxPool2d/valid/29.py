import torch
import torch.nn as nn

# Create an instance of MaxPool2d
maxpool = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)

# Define a random input tensor
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size 1, 3 channels, 4x4 image

# Apply the max pooling operation
output_tensor = maxpool(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Max Pooling:", output_tensor)