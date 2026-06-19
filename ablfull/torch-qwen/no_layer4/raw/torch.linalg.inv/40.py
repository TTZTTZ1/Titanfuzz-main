import torch

# Prepare valid input data
n = 4
A = torch.randn(n, n)
A = A @ A.T  # Ensure A is symmetric to be invertible

# Call the API
result = torch.linalg.inv(A)

print(result)