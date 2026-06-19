import torch
import torch.nn.functional as F

# Create a tensor
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)

# Normalize the tensor
normalized_x = F.normalize(x, p=2, dim=1)

print(normalized_x)