import torch

# Prepare valid input data
n = 5
A = torch.randn(n, n)

# Call the target API
result = torch.linalg.inv(A)