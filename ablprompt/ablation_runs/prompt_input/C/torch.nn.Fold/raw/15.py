import torch
from torch.nn import Fold

# Define the input dimensions
input_tensor = torch.randn(1, 64, 8, 8)  # Batch size=1, Channels=64, Height=8, Width=8

# Define the Fold parameters
kernel_size = (3, 3)
output_size = (8, 8)
stride = (1, 1)
padding = (1, 1)

# Create the Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 64, 8, 8])