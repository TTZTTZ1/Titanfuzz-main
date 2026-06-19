import torch

# Create two random tensors
a = torch.randn(4, 5)
b = torch.randn(5, 6)

# Compute the matrix product using einsum
result = torch.einsum('ij,jk->ik', a, b)

print(result)