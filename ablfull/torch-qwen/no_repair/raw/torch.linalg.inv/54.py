import torch

# Generate a square matrix
n = 4
A = torch.randn(n, n)

# Ensure A is invertible by making it non-singular
A[0, 0] += abs(A.min()) + 1

# Call torch.linalg.inv with A as input
result = torch.linalg.inv(A)