import torch
from torch.nn.functional import conv_transpose2d

# Example usage of conv_transpose2d
input_tensor = torch.randn(1, 3, 6, 6)
weight_tensor = torch.randn(3, 3, 4, 4)
output = conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1)

print(output.shape)  # Expected shape: [1, 3, 12, 12]