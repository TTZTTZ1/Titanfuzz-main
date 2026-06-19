import torch

# Task 2: Generate input data
n = 4
A = torch.randn(n, n, dtype=torch.float)

# Task 3: Call the API
result = torch.linalg.inv(A)