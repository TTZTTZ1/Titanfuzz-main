import torch

# Define two matrices
A = torch.randn(3, 4)
B = torch.randn(4, 5)

# Perform matrix multiplication using einsum
result = torch.einsum('ij,jk->ik', A, B)

print(result)