import torch

# Define input dimensions
input_tensor = torch.randn(1, 96, 8, 8)

# Define Fold parameters
kernel_size = (3, 3)
output_size = (8, 8)
stride = (1, 1)
padding = (1, 1)
dilation = (1, 1)

# Create Fold layer
fold = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation)

# Apply Fold layer
output_tensor = fold(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 96, 8, 8])