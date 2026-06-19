import torch
import torch.nn.functional as F

# Create a tensor
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalize the tensor
normalized_tensor = F.normalize(tensor)

print(normalized_tensor)