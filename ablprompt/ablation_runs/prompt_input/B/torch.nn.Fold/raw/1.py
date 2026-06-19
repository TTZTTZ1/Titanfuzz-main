import torch
from torch.nn.modules.fold import Fold

# Define input dimensions
N = 1  # Batch size
C = 3  # Number of channels
input_size = (8, 8)  # Input spatial size
kernel_size = (2, 2)
stride = (2, 2)
padding = (1, 1)

# Create a random input tensor
input_tensor = torch.randn(N, C * kernel_size[0] * kernel_size[1], input_size[0] * input_size[1])

# Calculate output size
output_size = ((input_size[0] + 2 * padding[0] - dilation[0] * (kernel_size[0] - 1) - 1) // stride[0] + 1,
               (input_size[1] + 2 * padding[1] - dilation[1] * (kernel_size[1] - 1) - 1) // stride[1] + 1)

# Initialize Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)