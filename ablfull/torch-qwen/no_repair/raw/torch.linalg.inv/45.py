import torch

# Prepare valid input data
n = 4
A = torch.randn(n, n)
out = None

# Call the target API
result = torch.linalg.inv(A, out=out)