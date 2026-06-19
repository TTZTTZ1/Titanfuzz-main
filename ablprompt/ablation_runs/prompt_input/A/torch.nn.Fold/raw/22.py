import torch
from torch.nn.modules.fold import Fold

# Create an input tensor
input_tensor = torch.randn(1, 3, 28, 28)

# Define the Fold parameters
output_size = (56, 56)
kernel_size = 4
stride = 2
padding = 0

# Create a Fold layer
fold_layer = Fold(output_size=output_size, kernel_size=kernel_size, stride=stride, padding=padding)

# Apply the Fold layer to the input tensor
output_tensor = fold_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 3, 56, 56])