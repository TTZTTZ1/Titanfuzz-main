import torch

# Create two random matrices
A = torch.randn(5, 3)
B = torch.randn(3, 7)

# Perform matrix multiplication
C = torch.mm(A, B)

print(C)