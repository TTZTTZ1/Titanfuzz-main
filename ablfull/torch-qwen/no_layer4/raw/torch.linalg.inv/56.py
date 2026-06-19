import torch

# Generate valid input data
n = 4
A = torch.randn(n, n)
A_inv = torch.linalg.inv(A)

print(A_inv)