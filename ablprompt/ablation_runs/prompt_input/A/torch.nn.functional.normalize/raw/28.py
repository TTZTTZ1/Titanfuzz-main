import torch
import torch.nn.functional as F

# Create a tensor
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)

# Normalize the tensor
normalized_tensor = F.normalize(tensor, p=2, dim=1)

print(normalized_tensor)