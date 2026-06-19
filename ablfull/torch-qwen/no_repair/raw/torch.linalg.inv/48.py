import torch

# Prepare input data
n = 4
A = torch.randn(n, n)
A = A @ A.t() + torch.eye(n) * 0.5  # Ensure A is positive definite for inv()

# Call the API
result = torch.linalg.inv(A)