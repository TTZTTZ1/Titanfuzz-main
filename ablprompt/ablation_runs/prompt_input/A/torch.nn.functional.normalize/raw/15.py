import torch
import torch.nn.functional as F

# Create a random tensor
x = torch.randn(3, 4)

# Normalize the tensor along dimension 1
normalized_x = F.normalize(x, p=2, dim=1)

print(normalized_x)