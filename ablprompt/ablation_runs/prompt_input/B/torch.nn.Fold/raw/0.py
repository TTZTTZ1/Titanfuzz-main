import torch

# Define input tensor dimensions
N = 1  # Batch size
C = 3  # Number of channels
L = 64  # Total number of blocks

# Define Fold parameters
output_size = (8, 8)
kernel_size = (2, 2)
stride = (2, 2)
padding = (0, 0)
dilation = (1, 1)

# Create input tensor
input_tensor = torch.randn(N, C * kernel_size[0] * kernel_size[1], L)

# Create Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: (1, 3, 8, 8)