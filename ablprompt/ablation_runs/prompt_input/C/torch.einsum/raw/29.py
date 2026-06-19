import torch

# Create two random tensors
a = torch.randn(4, 5)
b = torch.randn(5, 6)

# Use torch.einsum to compute the matrix product
result = torch.einsum('ij,jk->ik', a, b)

print(result)