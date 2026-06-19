import torch
from torch import nn

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply log_softmax along dimension 1
output_tensor = nn.functional.log_softmax(input_tensor, dim=1)

print(output_tensor)