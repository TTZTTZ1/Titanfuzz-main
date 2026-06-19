import torch

# Prepare valid input data
n = 4
A = torch.randn(n, n)

# Call the API
result = torch.linalg.det(A)
print(result)