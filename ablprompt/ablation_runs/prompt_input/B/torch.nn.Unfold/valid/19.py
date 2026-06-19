import torch
from torch.nn import Unfold

# Create a random input tensor
input_tensor = torch.randn(1, 1, 5, 5)

# Define the Unfold layer
unfold = Unfold(kernel_size=3, stride=1, padding=1)

# Apply the Unfold layer to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)