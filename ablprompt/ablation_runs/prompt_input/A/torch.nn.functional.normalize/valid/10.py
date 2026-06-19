import torch
import torch.nn.functional as F

# Example tensor
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Normalizing the tensor
normalized_x = F.normalize(x, p=2.0)

print("Original Tensor:", x)
print("Normalized Tensor:", normalized_x)