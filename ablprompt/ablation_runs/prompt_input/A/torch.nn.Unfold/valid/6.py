import torch
import torch.nn as nn

# Define a tensor
input_tensor = torch.randn(1, 1, 3, 3)

# Create an Unfold layer
unfold = nn.Unfold(kernel_size=2, stride=1, padding=0)

# Apply the Unfold operation
output_tensor = unfold(input_tensor)

print(output_tensor)