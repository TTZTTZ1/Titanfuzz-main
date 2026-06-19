import torch
import torch.nn.functional as F

# Example tensor
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalizing the tensor along dimension 1
normalized_x = F.normalize(x, p=2.0, dim=1)

print(normalized_x)