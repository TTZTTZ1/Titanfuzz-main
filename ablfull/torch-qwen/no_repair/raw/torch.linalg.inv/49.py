import torch

# Prepare valid input data
n = 4
A = torch.randn(n, n)
A_inv = torch.linalg.inv(A)

# Call the API
result = torch.linalg.inv(A, out=A_inv)