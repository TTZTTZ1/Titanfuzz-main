import torch
from torch.nn import Unfold

# Example input tensor (batch of images)
input_tensor = torch.randn(1, 3, 8, 8)

# Define the Unfold layer
unfold = Unfold(kernel_size=3, stride=2, padding=1)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)  # Expected output shape: [1, 27, 16]