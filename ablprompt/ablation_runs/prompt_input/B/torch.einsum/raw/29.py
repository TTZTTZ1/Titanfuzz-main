import torch

# Create two random matrices
A = torch.randn(3, 4)
B = torch.randn(4, 5)

# Compute the product of A and B using einsum
result = torch.einsum('ij,jk->ik', A, B)

print(result)