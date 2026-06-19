import torch

# Generate a random symmetric positive definite matrix
n = 4
A = torch.randn(n, n)
A = A @ A.t() + n * torch.eye(n)

# Compute the inverse of A
inv_A = torch.linalg.inv(A)