import torch

# Generate input data
n = 4
A = torch.randn(n, n)
inv_A = torch.linalg.inv(A)

# Call the API
result = torch.linalg.inv(A, out=inv_A)