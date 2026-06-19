import torch
import torch.nn.functional as F

# Example tensor to normalize
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalizing the tensor
normalized_tensor = F.normalize(tensor, p=2, dim=1)

print(normalized_tensor)