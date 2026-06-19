import torch

# Task 2: Generate input data
A = torch.randn(3, 3, dtype=torch.double)

# Task 3: Call the API
result = torch.linalg.inv(A)