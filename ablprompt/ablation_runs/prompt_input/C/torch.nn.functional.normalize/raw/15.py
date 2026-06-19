import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Normalize the tensor along dimension 1 using L2 norm
normalized_tensor = F.normalize(input_tensor, p=2.0, dim=1, eps=1e-12)

print("Original Tensor:", input_tensor)
print("Normalized Tensor:", normalized_tensor)