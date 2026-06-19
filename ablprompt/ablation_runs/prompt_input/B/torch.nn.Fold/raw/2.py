import torch

# Define input tensor dimensions
N = 1  # Batch size
C = 3  # Number of channels
L = 64  # Total number of blocks
kernel_size = (2, 2)
output_size = (8, 8)

# Create a random input tensor
input_tensor = torch.randn(N, C * kernel_size[0] * kernel_size[1], L)

# Initialize Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=(1, 1))

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)