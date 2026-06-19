import torch

# Generate input data
n = 5
A = torch.randn(n, n)

# Call the API
inv_A = torch.linalg.inv(A)