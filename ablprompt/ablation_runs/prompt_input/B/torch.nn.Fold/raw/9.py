import torch
from torch.nn import Fold

# Example input tensor
input_tensor = torch.randn(1, 96, 8)

# Define the Fold layer
unfold = Fold(output_size=(4, 4), kernel_size=2, stride=2, padding=0, dilation=1)

# Apply the Fold layer
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected shape: [1, 24, 4, 4]