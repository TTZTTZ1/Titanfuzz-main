import torch
from torch.nn import functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Normalize the tensor along dimension 2 using L1 norm
normalized_tensor = F.normalize(input_tensor, p=1.0, dim=2, eps=1e-6)

print(normalized_tensor)