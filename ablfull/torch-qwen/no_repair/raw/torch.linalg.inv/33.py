import torch

# Task 2: Generate input data
n = 5
A = torch.randn(n, n)

# Task 3: Call the API torch.linalg.inv
result = torch.linalg.inv(A)