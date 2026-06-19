import torch
from torch.nn import Fold

# Define input tensor dimensions
N = 2  # batch size
C = 3  # channels
input_size = (8, 8)
kernel_size = (2, 2)
output_size = (4, 4)

# Create a random input tensor
input_tensor = torch.randn(N, C * kernel_size[0] * kernel_size[1], input_size[0] * input_size[1])

# Initialize Fold layer
fold = Fold(output_size=output_size, kernel_size=kernel_size, stride=kernel_size)

# Apply Fold layer
output_tensor = fold(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)