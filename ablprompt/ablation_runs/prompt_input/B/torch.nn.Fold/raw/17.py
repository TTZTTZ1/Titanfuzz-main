import torch

# Define input dimensions
input_tensor = torch.randn(1, 96, 8)

# Define Fold parameters
output_size = (16, 16)
kernel_size = (3, 3)
stride = (2, 2)
padding = (1, 1)
dilation = (1, 1)

# Create Fold layer
fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)