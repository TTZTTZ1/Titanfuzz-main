import torch

# Create two example tensors
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Use torch.einsum to compute the matrix product
result = torch.einsum('ij,jk->ik', a, b)

print(result)