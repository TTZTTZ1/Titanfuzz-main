import torch

# Generate a random square matrix
n = 4
A = torch.randn(n, n)

# Call torch.linalg.inv
result = torch.linalg.inv(A)