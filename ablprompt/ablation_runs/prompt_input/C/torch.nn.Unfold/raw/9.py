import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 6, 6)

# Define the Unfold layer
unfold = nn.Unfold(kernel_size=3, stride=1, padding=1)

# Apply the Unfold operation
output_tensor = unfold(input_tensor)

print(output_tensor.shape)