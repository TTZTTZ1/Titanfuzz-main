import torch

# Create a random input tensor
input_tensor = torch.randn(1, 96, 8)

# Define Fold parameters
kernel_size = (3, 3)
output_size = (8, 8)
stride = (2, 2)
padding = (1, 1)

# Initialize Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply Fold layer to input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 256, 8, 8])