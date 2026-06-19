import torch

# Define two matrices and a vector
A = torch.randn(3, 4)
B = torch.randn(4, 5)
v = torch.randn(5)

# Compute the matrix-matrix product followed by the matrix-vector product
result = torch.einsum('ij,jk->ik', A, B) @ v

print(result)