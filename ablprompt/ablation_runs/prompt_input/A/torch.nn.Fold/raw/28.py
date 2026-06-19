import torch
import torch.nn as nn

# Create an input tensor
input_tensor = torch.randn(1, 4, 8, 8)

# Define the Fold layer
unfold = nn.Unfold(kernel_size=2, stride=2, padding=0)

# Apply the Unfold operation to get the unfolded view of the input tensor
output_tensor = unfold(input_tensor)

print(output_tensor.shape)