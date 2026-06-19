import torch

# Generate a random square matrix
n = 4
A = torch.randn(n, n)

# Call the API
result = torch.linalg.inv(A)