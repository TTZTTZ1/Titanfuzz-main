import torch

# Define input dimensions and parameters
input_tensor = torch.randn(1, 64, 8, 8)  # Example input tensor of shape (N, C * ∏(kernel_size), L)
output_size = (16, 16)
kernel_size = (3, 3)
stride = (2, 2)

# Create a Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected shape: (1, 64, 16, 16)