import torch

# Prepare input data
n = 3
A = torch.randn(n, n)

# Call the API
result = torch.linalg.inv(A)