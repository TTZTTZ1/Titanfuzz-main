import torch
import torch.nn.functional as F

# Create a random tensor
tensor = torch.randn(3, 4)

# Normalize the tensor
normalized_tensor = F.normalize(tensor, p=2, dim=1)

print(normalized_tensor)