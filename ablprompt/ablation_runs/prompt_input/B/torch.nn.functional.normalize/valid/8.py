import torch
from torch.nn.functional import normalize

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Normalize the tensor along dimension 1 using the default Euclidean norm
normalized_tensor = normalize(input_tensor, p=2.0, dim=1)

print(normalized_tensor)