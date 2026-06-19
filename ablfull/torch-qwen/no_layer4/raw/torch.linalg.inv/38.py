import torch

# Generate valid input data
n = 5
A = torch.randn(n, n)

# Call the API
result = torch.linalg.inv(A)