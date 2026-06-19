import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply log_softmax along the last dimension
output_tensor = nn.functional.log_softmax(input_tensor, dim=1)

print(output_tensor)