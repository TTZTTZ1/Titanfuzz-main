import torch

# Generate a random square matrix
n = 4
A = torch.randn(n, n)

# Ensure the input data satisfies the constraints
inv_A = torch.linalg.inv(A)