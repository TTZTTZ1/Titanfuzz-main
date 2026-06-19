import torch

# Define two matrices
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Compute the matrix product using einsum
result = torch.einsum('ij,jk->ik', a, b)

print(result)