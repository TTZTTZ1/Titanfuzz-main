import torch

# Define two matrices
A = torch.randn(3, 4)
B = torch.randn(4, 5)

# Compute the matrix product C = A @ B using einsum
C = torch.einsum('ij,jk->ik', A, B)

print(C)