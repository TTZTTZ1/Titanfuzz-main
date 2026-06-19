import torch
from torch.nn.functional import normalize

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Normalize the tensor using L2 norm along dimension 1
normalized_tensor = normalize(input_tensor, p=2.0, dim=1, eps=1e-12)

print(normalized_tensor)