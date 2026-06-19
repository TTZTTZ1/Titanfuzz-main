import torch
from torch.nn import functional as F

# Create a tensor
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalize the tensor
normalized_tensor = F.normalize(tensor, p=2.0)

print(normalized_tensor)