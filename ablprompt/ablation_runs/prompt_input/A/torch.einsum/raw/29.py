import torch

# Create some example tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Use torch.einsum to perform a matrix multiplication
result = torch.einsum('ij,jk->ik', a, b)

print(result)