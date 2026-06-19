import torch

# Generate input data
n = 5
A = torch.randn(n, n, dtype=torch.float)

# Call the API
result = torch.linalg.inv(A)