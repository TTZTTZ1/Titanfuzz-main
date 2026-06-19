import torch
from torch.nn.functional import normalize

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Normalize the tensor along dimension 1 using L2 norm
normalized_tensor = normalize(input_tensor, p=2.0, dim=1)

print("Original Tensor:\n", input_tensor)
print("Normalized Tensor:\n", normalized_tensor)