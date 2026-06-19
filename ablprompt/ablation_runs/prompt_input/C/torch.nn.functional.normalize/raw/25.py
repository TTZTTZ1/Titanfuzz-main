import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Normalize the tensor along dimension 1 using L2 norm
normalized_tensor = F.normalize(input_tensor, p=2.0, dim=1, eps=1e-12)

print(normalized_tensor)