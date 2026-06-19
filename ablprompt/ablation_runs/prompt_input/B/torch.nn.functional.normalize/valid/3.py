import torch
from torch.nn.functional import normalize

# Create a random tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Normalize the tensor along dimension 1 using the Euclidean norm
normalized_tensor = normalize(input_tensor, p=2.0, dim=1, eps=1e-12)

print("Original Tensor:\n", input_tensor)
print("Normalized Tensor:\n", normalized_tensor)