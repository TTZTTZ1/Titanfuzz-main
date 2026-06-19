import torch
from torch import nn

# Define the input tensor
input_tensor = torch.randn(1, 3, 4, 4)

# Create an instance of Unfold
unfold = nn.Unfold(kernel_size=2, stride=1, padding=0)

# Apply Unfold to the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor)