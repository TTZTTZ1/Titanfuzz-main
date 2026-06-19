import torch

# Generate input data
n = 4
A = torch.randn(n, n, dtype=torch.float)

# Call the API
result = torch.linalg.inv(A)