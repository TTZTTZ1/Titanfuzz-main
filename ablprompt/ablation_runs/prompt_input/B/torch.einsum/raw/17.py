import torch

# Define two matrices and a vector
A = torch.randn(3, 4)
B = torch.randn(4, 5)
v = torch.randn(4)

# Compute the result of the operation A * B * v^T
result = torch.einsum('ab,bc,c->a', A, B, v)

print(result)