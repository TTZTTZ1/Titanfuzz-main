import torch

# Prepare valid input data
n = 4
A = torch.randn(n, n, dtype=torch.float)

# Call the target API
result = torch.linalg.inv(A)