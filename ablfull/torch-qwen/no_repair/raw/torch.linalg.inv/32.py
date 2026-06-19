import torch

# Prepare input data
n = 4
A = torch.randn(n, n, dtype=torch.float64)

# Call the API
result = torch.linalg.inv(A)