import torch
from torch.nn.functional import softmax

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Apply softmax along dimension 1
output_tensor = softmax(input_tensor, dim=1)

print(output_tensor)