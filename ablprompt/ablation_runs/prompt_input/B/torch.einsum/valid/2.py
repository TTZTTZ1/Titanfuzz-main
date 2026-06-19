import torch

# Define two matrices
A = torch.randn(2, 3)
B = torch.randn(3, 4)

# Compute the matrix product using einsum
result = torch.einsum('ij,jk->ik', A, B)

print(result)