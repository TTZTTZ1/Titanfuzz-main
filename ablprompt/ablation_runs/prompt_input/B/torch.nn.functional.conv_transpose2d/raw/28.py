import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 6, 6)

# Define the weight tensor
weight_tensor = torch.randn(3, 3, 4, 4)

# Perform the 2D transposed convolution
output_tensor = F.conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1)

print(output_tensor.shape)  # Expected shape: [1, 3, 12, 12]