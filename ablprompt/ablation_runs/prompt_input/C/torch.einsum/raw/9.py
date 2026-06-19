import torch

# Create some example tensors
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Use torch.einsum to perform matrix multiplication
result = torch.einsum('ij,jk->ik', a, b)

print(result)