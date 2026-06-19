import torch

# Create two tensors for demonstration
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Use torch.einsum to perform a matrix multiplication
result = torch.einsum('ij,jk->ik', a, b)

print(result)