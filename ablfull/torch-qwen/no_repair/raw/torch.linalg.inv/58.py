import torch

# Generate valid input data
n = 4
A = torch.randn(n, n, dtype=torch.double)

# Call the API
result = torch.linalg.inv(A)