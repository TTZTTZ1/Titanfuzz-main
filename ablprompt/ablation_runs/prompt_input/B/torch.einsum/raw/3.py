import torch

# Create two random tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Use einsum to compute the matrix product
result = torch.einsum('ij,jk->ik', a, b)

print(result)